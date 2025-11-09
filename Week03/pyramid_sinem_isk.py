def calculate_pyramid_height(number_of_blocks):
    height = 0
    used_blocks = 0

    while True:
        next_layer = height + 1  
        if used_blocks + next_layer > number_of_blocks:
            break
        used_blocks += next_layer
        height += 1
    return height

if __name__ == "__main__":
    number_of_blocks = int(input("Kaç blok var: "))
    height = calculate_pyramid_height(number_of_blocks)
    print("Piramidin yüksekliği:", height)
