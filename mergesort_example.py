from pygame_list_visualizer import visualize_list
import random
random_numbers = []
for i in range(50):
    random_numbers.append(random.randint(0,410))
                     #      WIDTH, HEIGHT, numbers(a list), scale, window_name, matching_list(put None if want to display in white)
screen = visualize_list(window_name="merge sort")
screen.attach_list(random_numbers)
screen.list_compare(sorted(random_numbers))
screen.update_screen()
#from https://www.geeksforgeeks.org
def merge(arr, l, m, r, screen):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        screen.update_screen()
        screen.clock.tick(30)

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        screen.update_screen()
        screen.clock.tick(30)
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        screen.update_screen()
        screen.clock.tick(30)

def mergeSort(arr, l, r, screen):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m, screen)
        mergeSort(arr, m + 1, r, screen)
        merge(arr, l, m, r, screen)
mergeSort(random_numbers, 0, len(random_numbers) - 1, screen)



while True:
    screen.clock.tick(1)
