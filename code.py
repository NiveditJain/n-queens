def cost(state):
    count = 0

    if(len(state) != 8):
        return None

    for i in range(8):
        for j in range(i+1, 8):
            if state[i] == state[j]:
                count = count + 1
            if abs(state[j] - state[i]) ==  abs(j - i):
                count = count + 1

    return count

state = [6, 7, 2, 8, 3, 4, 1, 5]

min_state = state
min_cost = cost(state)
print(state, min_cost)

while(min_cost!=0):

    state = min_state.copy()

    for i in range(8):
        for j in range(1, 9):
            temp_state = state[:i] + [j] + state[i+1:]
            temp_cost = cost(temp_state)
            if(temp_cost < min_cost):
                min_state = temp_state
                min_cost = temp_cost

    print(min_state, min_cost)