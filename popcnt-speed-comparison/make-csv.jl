function get_data_hash()
    f = open("data-0")
    line = readline(f)
    h = Dict{String, Array{Int}}()
    while line != ""
        name, time = split(line, ":")
        if !haskey(h, name)
            h[name] = Array(Int, 0)
        end
        push!(h[name], int(time))
        line = readline(f)
    end
    close(f)
    return h
end

function print_sideways_header(h, delta::Int)
    row_length = -1
    some_row = Array(Int)
    for (_, row) in h
        if row_length == -1
            row_length = length(row)
        else
            assert(row_length == length(row))
        end
    end
    
    print("bytes")
    current = 0
    for i in 1:row_length
        current += delta * 8
        print(",$(current)")
    end
    print("\n")
end

function print_sideways_data_hash(h)
    for (name, times) in h
        print("$name,$(join(times,','))\n")
    end
end

# h = get_data_hash()
# print_sideways_header(h, 128)
# print_sideways_data_hash(h)

f = open("data-1")
line = readline(f)
first_name, _ = split(line, ":")
print("bytes")
print(",$first_name")
line = readline(f)
name, _ = split(line, ":")
while name != first_name
    print(",$name")
    line = readline(f)
    name, _ = split(line, ":")
end

seek(f, 0)
line = readline(f)
delta = 128*8
bytes = 0
while line != ""
    name, time = split(line, ":")
    if name == first_name
        print("\n")
        bytes += delta
        print(bytes)
    end
    print(",$(chomp(time))")
    line = readline(f)
end
