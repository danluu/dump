# This is a total hack. You probably don't want to read this.

# Increment a count in a dict.
# This has its own function to encapsulate some heinous bug workaround
# code.
function increment_word(words::Dict{String,Int}, word::String)
    if !haskey(words, word)
        words[word] = 0
    end

    # Workaround for julia hash on unicode string bug
    # Note that this code non-determnisically hits a julia bug involving
    # exceptions which may cause this exception to be uncaught.
    try 
        words[word] += 1
    catch
        # println("DICT LOOKUP FAIL (uncode string bug?)------------------------")
        # println(w)
    end
end

# DefaultDict, basically.
function increment_author_word(authors::Dict{String,Dict{String,Int}}, word::String, author::String)
    if !haskey(authors, author)
        authors[author] = Dict{String,Int}()
    end

    increment_word(authors[author], word)
end

# Ignore email addresses
function bogus_word(word::String)
    ismatch(r"^<.*>$", word)
end

# Strip stuff like commas.
# Sort of bad, since these can demarcate things inside real identifiers.
# But it also creates a ton of noise and doing this in a smart way seems annoying.
function strip_punct(word::String)
    word = replace(word, r"\(","")
    word = replace(word, r"\)","")
    word = replace(word, r"\.","")
    word = replace(word, r",","")
    word = replace(word, r"\"","")
    word = replace(word, r"\*","")
    word = replace(word, r"'","")
    word = replace(word, r"`","")
    word = replace(word, r"!","")
    word = replace(word, r";","")
    word = replace(word, r":","")
    word = replace(word, r"\[","")
    word = replace(word, r"\]","")
    word = replace(word, r"^1$","")
end

# Takes a full commit message, minus the commit hash.
# TODO: handle old-style merge commits with From:
function process_chunk(chunk::String, all_words::Dict{String,Int}, author_words::Dict{String,Dict{String,Int}}, num_author_commits::Dict{String,Int})
    exists_in_chunk = Dict{String, Bool}()

    # Ignore merge commits.
    if ismatch(r"^Merge:", chunk)
        return 0 # number of chunks processed = 0
    end
    
    author = ""
    author_match = match(r"^Author.*<(.*)@.*>\n",chunk)
    if author_match != nothing
        author = lowercase(author_match.captures[1])
    else
        # fails on non-standard email address formats. Not many of these.
        # Ignoring for now.
    end

    # println("DEBUG--------------------------CHUNK")
    first_line = search(chunk, '\n')                # strip Author
    second_line = search(chunk, '\n', first_line+1) # strip Date

    # search returns a BoundsError if not found, so we have to try/catch this.
    # Seems like an API mistake/bug since this inconsistent with other 'search'
    # methods.
    chunk_words = Array(String,0)
    try
        sign_off = search(chunk,r"Signed-off-by:")[1]-1
        chunk_words = split(chunk[second_line:sign_off])
    catch
        chunk_words = split(chunk[second_line:end])
    end

    increment_word(num_author_commits,author)

    # only count each word once per chunk.
    for w in chunk_words
        if !bogus_word(w)
            exists_in_chunk[lowercase(strip_punct(w))] = true
        end
        # increment_author_word(author_words, w, author)
    end

    for (w,_) in exists_in_chunk
            increment_word(all_words, w)
            increment_author_word(author_words, w, author)
    end
    return 1 # number of chunks processed = 1
end

# Take dict and return a sorted array of (String, Int) tuples, sorted by the Int.
function sort_authors(num_author_commits::Dict{String,Int})
    author_arr = Array((String,Int), length(num_author_commits))
    i = 1
    for (author,num) in num_author_commits
        author_arr[i] = (author,num)
        i += 1
    end
    sort!(author_arr,by= x -> -x[2])
end

# Horribly abusing tf-idf. This is really not what it's intended for.
function top_words_for_author(all_words::Dict{String,Int}, their_words::Dict{String,Int}, author::String, num_words::Int)
    word_arr = Array((String,Float64), length(their_words))
    i = 1
    for (word, count) in their_words
        try 
            # "1+" is to avoid degenerate case that should never happen anyway.
            ratio = (1+num_words) / all_words[word]
            idf = log(ratio)
            tf_idf = count * idf
            word_arr[i] = (word, tf_idf)

        catch wat
            # try/catch is workaround for unicode string hash bug
            word_arr[i] = (word, 0)
        end
        i += 1
    end

    print("$author")
    sort!(word_arr,by= x -> -x[2])

    i = 0
    for (word, count) in word_arr
        print(",$word")
        i += 1
    end
    println("")
end

# Reads a git commit log. Does some magic that assumes linux kernel format, but shouldn't break on an arbitrary
# log
function read_log(fname::String, by_author::String)
    author_words = Dict{String,Dict{String,Int}}()
    all_words = Dict{String,Int}()
    num_author_commits = Dict{String,Int}()
    num_chunks = 0
    process_each_author = bool(int(by_author)) # horrible hack to convert arg to bool. 0 = false.

    f = open(fname)
    chunk = ""
    line = readline(f)
    while line != ""
        line = readline(f)
        # Start of new commit. Previous chunk is complete and should be processed.
        if ismatch(r"^commit ", line)
            num_chunks += process_chunk(chunk, all_words, author_words, num_author_commits)
            chunk = ""
        else
            chunk *= line
        end
    end
    
    if process_each_author
        sorted_authors = sort_authors(num_author_commits)
        for (author,count) in sorted_authors
            top_words_for_author(all_words, author_words[author], author, num_chunks)
        end
    else
        sorted_words = sort_authors(all_words)
        for (k,v) in sorted_words
            println("$k,$v")
        end
    end
end

print(read_log(ARGS[1], ARGS[2]))
