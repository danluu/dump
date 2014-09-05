const test_dir = "jl_input"

function generate_tests(n::Int)
    for i in 1:n
        len = rand(1:2^19-5000)
        f = open("$(test_dir)/$(i)","w")
        write(f, randstring(len))
        close(f)
    end
end

# generate_tests(2^12)

function bogus()
    potential_names = names(Base)
    name = potential_names[rand(1:end)]

    print(methods(eval(name)))
end

bogus()
