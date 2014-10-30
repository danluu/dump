# Takes a full commit message, minus the commit hash.
function process_chunk(chunk::String)
    # TODO: handle old-style merge commits with From:

    # Ignore merge commits.
    if match(r"^Merge:", chunk)
        return
    end
    
    
end

function read_log(fname::String)
    f = open(fname)
    chunk = ""
    line = readline(f)
    while line != ""
        line = readline(f)
        # Start of new commit. Previous chunk is complete and should be processed.
        if match(r"^commit ", line)
            process_chunk(chunk)
            chunk = ""
        else
            # TODO: add line to chunk here.
        end
    end    
end

print(read_log("linux-log-mini-recent"))
