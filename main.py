from pyscript import display

comarts_students = {'AJ', 'Carl', 'Shino'}
ssclub_students = {'AJ', 'Carl', 'Miguel'}

display(f"Students in atleast one club are: {comarts_students | ssclub_students}", target='output1') # union
display(f"Students in both clubs are: {comarts_students & ssclub_students}", target='output2') # intersection
display(f"Students in the first club are: {comarts_students - ssclub_students}", target='output3') # difference
display(f"Students in the second club are: {ssclub_students - comarts_students}", target='output4') # difference
display(f"Students in exactly one club are: {comarts_students ^ ssclub_students}", target='output5') # symmetric difference
