	# Autograder

# This will attempt to perform intended tasks for SortedList, using Sortables.
# For each task, the autograder will:
#  - Define some expected behavior for some use case
#  - Perform the use case
#  - Award "points" if the result is as expected
#  - Either not award points (not too bad) or cause an error (pretty bad) if the result is not as expected
#    NOTE: Exception handling here could manage these errors, but it can be helpful to see them as well!

# This is a script to do the tests and print out what's happening
def singleTest(desc, target, val, pts):
	print("AUTOGRADER: " + desc)
	print(" - Expected Value: " + str(target))
	print(" - Observed Value: " + str(val))
	score = 0
	if (val == target):
		score = 5
		pts = pts + 5
	print("POINTS: This section: " + str(score).zfill(2) + "/05 Total: " + str(pts).zfill(3) + "/100\n")	
	return pts

points = 0

print("\n --- AUTOGRADER: SortList ---\n")
from sortList import SortList
l = SortList(5)

print("\nAUTOGRADER: Singleton List Testing: 20 pts\n")
points = singleTest("Checking SortList (5).size()", 1, l.size(), points)
points = singleTest("Checking SortList(5).index(0)", 5, l.index(0), points)
points = singleTest("Checking SortList(5).index(1)", None, l.index(1), points)
ltest = l.insert(3)
points = singleTest("Checking SortList(5).insert(3) != SortList(5)", False, str(l) == str(ltest), points)

print("\nAUTOGRADER: Doubleton List Testing: 35 pts\n")
l = ltest
points = singleTest("Checking SortList ((3)->(5)).size()", 2, l.size(), points)
points = singleTest("Checking SortList ((3)->(5)).index(0)", 3, l.index(0), points)
points = singleTest("Checking SortList ((3)->(5)).index(1)", 5, l.index(1), points)
points = singleTest("Checking SortList ((3)->(5)).index(2)", None, l.index(2), points)
points = singleTest("Checking SortList ((3)->(5)).contains(3)", True, l.contains(3), points)
points = singleTest("Checking SortList ((3)->(5)).contains(4)", False, l.contains(4), points)
points = singleTest("Checking SortList ((3)->(5)).contains(5)", True, l.contains(5), points)

print("\nAUTOGRADER: Remove/Insert Doubleton Testing: 20 pts\n")
l = l.remove(5)
points = singleTest("Checking that .index(0) is 3 after .remove(5)", 3, l.index(0), points)
points = singleTest("Checking that .index(1) is None after .remove(5)", None, l.index(1), points)
l = l.insert(4)
points = singleTest("Checking that .index(1) == 4 after .insert(4)", 4, l.index(1), points)
points = singleTest("Checking that .index(0) == 3 after .insert(4)", 3, l.index(0), points)
points = singleTest("Checking that .index(2) is None after .insert(4)", None, l.index(2), points)

print("\nAUTOGRADER: Remove/Insert General Testing: 20 pts\n")
l = SortList(5)
l = l.insert(3)
l = l.insert(7)
points = singleTest("For SNL(3->5->7) .index(0) == 3, .index(1) == 5, and .index(2) = 7", [3, 5, 7], [l.index(0), l.index(1), l.index(2)], points)
l = l.remove(5)
points = singleTest("Checking internal removal with SNL(3->5->7).remove(5).contains(5)", False, l.contains(5), points)
l = l.insert(5)
points = singleTest("Checking internal re-insertion with .insert(5)", [3, 5, 7], [l.index(0), l.index(1), l.index(2)], points)
l = l.remove(3)
l = l.remove(5)
l = l.remove(7)
points = singleTest("Removing all elements should give None", None, l, points)
