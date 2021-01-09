fname="../road_datasets/graphs/amsterdam.graph"
with open(fname, 'r') as f:
    lines=f.readlines()
    print(len(lines))
    for l in lines:
        print(l)
        break
    
