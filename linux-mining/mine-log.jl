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

function increment_author_word(authors::Dict{String,Dict{String,Int}}, word::String, author::String)
    if !haskey(authors, author)
        authors[author] = Dict{String,Int}()
    end

    increment_word(authors[author], word)
end

# Takes a full commit message, minus the commit hash.
function process_chunk(chunk::String, all_words::Dict{String,Int}, author_words::Dict{String,Dict{String,Int}}, num_author_commits::Dict{String,Int})
    # TODO: handle old-style merge commits with From:

    # Ignore merge commits.
    if ismatch(r"^Merge:", chunk)
        return
    end
    
    author = ""

    # println("DEBUG--------------------------CHUNK")
    chunk_words = split(chunk)
    author_match = match(r"^Author.*<(.*)@.*>\n",chunk)
    if author_match != nothing
        author = author_match.captures[1]
    else
        # fails on non-standard email address formats. Not many of these.
        # Ignoring for now.
        # println("AUTHOR MATCH FAIL------------------------")
        # println(chunk)
    end
    # TODO: attribute some commits to other people.
    increment_word(num_author_commits,author)

    for w in chunk_words
        increment_word(all_words, w)
        increment_author_word(author_words, w, author)
    end
end

function sort_authors(num_author_commits::Dict{String,Int})
    # Make an array and use built-in sort on number of commits per author
    author_arr = Array((String,Int), length(num_author_commits))
    i = 1
    for (author,num) in num_author_commits
        author_arr[i] = (author,num)
        i += 1
    end
    sort!(author_arr,by= x -> -x[2])
end

function read_log(fname::String)
    author_words = Dict{String,Dict{String,Int}}()
    all_words = Dict{String,Int}()
    num_author_commits = Dict{String,Int}()

    f = open(fname)
    chunk = ""
    line = readline(f)
    while line != ""
        line = readline(f)
        # Start of new commit. Previous chunk is complete and should be processed.
        if ismatch(r"^commit ", line)
            process_chunk(chunk, all_words, author_words, num_author_commits)
            chunk = ""
        else
            chunk *= line
        end
    end
    
    sorted_authors = sort_authors(num_author_commits)
end

#println(read_log("linux-log-mini-recent"))
#println(read_log("linux-log-mini-old"))
print(read_log("linux-log"))
