# Convert first N columns of a csv to markdown table format.

function read_csv(args)
    fname = args[1]  # all.csv, tf-only.csv, etc.
    max_col = 2
    max_row = 40
    
    f = open(fname)
    line = readline(f)
    line_num = 1
    while line != "" && line_num <= max_row
        chunks = split(line,',')
        middle_cols = join(chunks[1:max_col], " | ") # assume max_col <= length
        println("| $middle_cols |")
        line = readline(f)
        line_num += 1
    end
end

read_csv(ARGS)
