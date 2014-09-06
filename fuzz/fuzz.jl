const test_dir = "jl_input"
const max_rand_string_len = 2^16

function generate_rand_strings(n::Int)
    for i in 1:n
        len = rand(1:2^19-5000)
        f = open("$(test_dir)/$(i)","w")
        write(f, randstring(len))
        close(f)
    end
end

# generate_rand_strings(3)

function checkable_name(name)
    typeof(eval(name)) == Function && isgeneric(eval(name))
#    || typeof(eval(name)) == DataType # killing for now because we can't call start on DataType 'methods'
end

function bogus()
    potential_names = sort(names(Base)) # names are returned in a random order.
#    name = potential_names[rand(1:end)]
    potential_names = filter(checkable_name, potential_names)

    for name in potential_names
 #       print("$name\n")
        methods_of_name = methods(eval(name))
        some_method = start(methods_of_name)
        print("$some_method type:$(typeof(some_method))\n")
#        print("  sig: $(some_method.sig) type:$(typeof(some_method.sig))\n")
        some_sig = some_method.sig
        print(generate_rand_data(some_sig))
    end

end

function generate_rand_data(x::String)
    return randstring(rand(1:max_rand_string_len))
end

function generate_rand_data(sig::Tuple)
    for t in sig
        print("  t: $t\n")
    end
end

bogus()

