conflicts = ['GW', 'GC']
visited = []

def create_graph():
    initial_state = 'FCGW|'
    return {initial_state: get_next_level(initial_state)}


def get_next_level(state):
    # generate all possible valid state transitions
    transitions = []
    east, west = state.split('|')
    is_east = 'F' in east
    current_side, other_side = (east.replace('F', ''), west) if is_east else (west.replace('F', ''), east)
    for companion in current_side:
        add_valid_transition(transitions, current_side.replace(companion, ''), other_side + 'F' + companion, is_east)
    add_valid_transition(transitions, current_side, other_side + 'F', is_east)
    return dict((transition, get_next_level(transition)) for transition in transitions)


def add_valid_transition(transitions, current, other, is_east):
    if is_east:
        transition = current + '|' + other
    else:
        transition = other + '|' + current
    # check validity
    if transition in visited:
        return transitions
    for conflict in conflicts:
        if all(c in current for c in conflict):
            return transitions
    visited.append(transition)
    return transitions.append(transition)


if __name__ == '__main__':
    graph = create_graph()
    print(graph)
