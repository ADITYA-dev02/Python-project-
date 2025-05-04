from mypackage import append1, adds2, add3

print("List append via __init__:", append1([10, 20], 30))
print("Set add via __init__:", adds2({5, 6}, 7))
print("Dict add via __init__:", add3({'x': 9}, 'y', 10))