# using Gadfly
using Dates
using DataFrames

function grab_pop(fname::String)
    f = open(fname)
    lines = readlines(f)
    pop_match = r"(\d+)\]"
    time_match = r"setTime\((\d+)\)"
    time_lines = filter(time_match, lines)
    data_lines = filter(pop_match, lines)
    data::Array{Int} = map(l -> int(match(pop_match, l).captures[1]), data_lines)
    # Not using DateTime because there's a bug in Gadfly that seems to be pretty old
    # that makes DateTime dataframes blow up. Not sure if/when it will be fixed.
    # times::Array{DateTime} = 
    # map(l -> 
    #     unix2datetime(int(match(time_match, l).captures[1]) / 1000),
    #     time_lines)
    times::Array{Int} = 
    map(l -> 
        int(match(time_match, l).captures[1]) / 1000,
        time_lines)
    
    df = DataFrame(x = times, y=data, label="Players")    
end

# function plot_junk(data::Array{Int})
#     mdata = map(x->min(1,x) , data)

#     sdata = [mean(data[i-118:i]) for i = 119:length(data)]
#     smdata = [mean(mdata[i-118:i]) for i = 119:length(mdata)]
#     plot(x=1:length(sdata), y=sdata, Geom.line, 
#          layer(Geom.smooth, Theme(default_color=color("red"))))

#     plot(x=1:length(smdata), y=smdata, Geom.line, 
#          layer(Geom.smooth, Theme(default_color=color("red"))))
# end

# grab_pop("raw.data")
