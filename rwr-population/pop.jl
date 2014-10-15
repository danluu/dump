using Gadfly

function grab_pop(fname::String)
    f = open(fname)
    lines = readlines(f)
    pop_match = r"(\d+)\]"
    data_lines = filter(pop_match, lines)
    data::Array{Int} = map(l -> int(match(pop_match, l).captures[1]), data_lines)
end

function plot_junk(data::Array{Int})
    sdata = [mean(data[i-118:i]) for i = 119:length(data)]
    plot(x=1:length(sdata), y=sdata, Geom.line, 
         layer(Geom.smooth, Theme(default_color=color("red"))))
end

grab_pop("raw.data")
