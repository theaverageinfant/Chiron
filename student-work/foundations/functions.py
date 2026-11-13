# Functions and returned values
# Write `intake_output(request, enabled, has_piece)` using your previous conditional. It should return a value rather than print inside the function. Call it for forward collection, a detected piece, reverse release, and disabled operation.
# Write your attempt below. See the course page for expected results.
def choose_output(request, enabled): # -> request
    if not enabled:
        return 0.0
    return request

result = choose_output(0.4, True)
print("Enabled:", result)
print("Disabled:", choose_output(0.4, False))

def intake_output(request, enabled, has_piece):  # -> request 
    if not enabled:
        return 0.0
    if has_piece and request > 0:
        return 0.0
    return request

print(intake_output(0.5, True, False))
print(intake_output(0.5, True, True))
print(intake_output(-0.5, True, True))
print(intake_output(-0.5, False, True))