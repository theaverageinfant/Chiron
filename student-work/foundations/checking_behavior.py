# Checking behavior with assertions
# Add clamping to your intake function. Write assertions for forward/no piece, forward/held piece, reverse/held piece, disabled, and requests outside both bounds.
# Write your attempt below. See the course page for expected results.
def clamp_request(request):
    if request > 1.0:
        return 1.0
    if request < -1.0:
        return -1.0
    return request

assert clamp_request(0.4) == 0.4
assert clamp_request(2.0) == 1.0
assert clamp_request(-2.0) == -1.0
assert clamp_request(1.0) == 1.0
print("All request checks passed.")


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

assert intake_output(0.5, True, False) == 0.5
assert intake_output(0.5, True, True) == 0.0
assert intake_output(-0.5, True, True) == -0.5
assert intake_output(-0.5, False, True) == 0.0
print("All intake checks passed.")