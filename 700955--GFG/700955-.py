# Function to join given bound_by and tag
def join_middle(bound_by, tag_name):
  # complete the statement below to return the string as required
  b=len(bound_by)
  return bound_by[:b//2 ] + tag_name + bound_by[b//2:  ]