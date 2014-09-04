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

function print_data_hash(h)
    for (name, times) in h
        print("$name,$(join(times,','))\n")
    end
end

h = get_data_hash()
print_data_hash(h)
