function err_result(s::String)
    beginswith(s, "# CAUGHT:")
end

function canonicalize_path(s::String)
    s = replace(s, r"/Users/danluu","")
    s = replace(s, r"/home/dluu","")
end

function check_logs(fname1::String, fname2::String)
    f1 = open(fname1)
    f2 = open(fname2)
    line1 = readline(f1)
    line2 = readline(f2)
    i = 0
    while line1 != ""  && line2 != ""
        i += 1
        println(i)
        line1 = canonicalize_path(line1)
        line2 = canonicalize_path(line2)
    	if err_result(line1) || err_result(line2)
            # maybe do something here.
        elseif line1 != line2
            print("MISMATCH $i\n$line1 $line2")
        end
        line1 = readline(f1)
        line2 = readline(f2)
    end
end

check_logs("log", "log-lin64")
