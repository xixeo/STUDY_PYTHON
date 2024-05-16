def print_models(unprinted_designs, complted_models):
    # 남은 게 없을 때까지 디자인을 출력
    # 출력한 디자인을 complted_models로 옮김
    while unprinted_designs:
      current_design = unprinted_designs.pop()
      print(f'printing model: {current_design}')
      completed_models.append(current_design)

def show_complted_models(complted_models):
    #완료된 디자인 표시
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
      print(completed_model)

# 출력할 디자인이 저장된 리스트
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_complted_models