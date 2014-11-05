# Take a CSV and produce a list of absolute and relative positons of a word.

function read_csv()
    fname = "all.csv"
    
    f = open(fname)
    line = readline(f)
    line_num = 1
    while line != ""
        chunks = split(line,',')
        num_words = length(chunks) - 1
        null_pos = find(x -> x == "fix", chunks)
        assert(length(null_pos) <= 1)
        if length(null_pos) > 0
            word_pos = null_pos[1] - 1
            assert(word_pos > 0)
            relative_pos = 1 - (word_pos / num_words) # percentile rank
            println("$line_num,$word_pos,$relative_pos")
        end
        line = readline(f)
        line_num += 1
    end
end

read_csv()
