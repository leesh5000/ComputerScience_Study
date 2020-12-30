# AVL Tree
# - BST의 경우, 저장순서에 따라 탐색성능에 큰 차이를 보인다. 예) 1부터 5까지 순서대로 저장 vs 3먼저 저장하고 1부터 5까지 저장
# - BST의 단점을 해결한 트리를 '균형잡힌트리'라고 하며, AVL, 2-3, 2-3-4, Red-Black, B Tree 등이 있다.
# - Balance Factor : AVL트리에서 균형의 정도를 표현하기 위해 사용, 왼쪽 서브트리의 높이 - 오른쪽 서브트리의 높이
# - Balance Factor의 절대값이 2이상인 경우, Rebalancing 진행
# - LL상태 : 왼쪽으로 자식노드 2개가 있는 상태
# - LL회전 : LL상태에서 균형을 잡기위해 필요한 회전으로, 균형지수가 2인 노드를 균형지수가 1인 노드의 오른쪽 자식노드로 만듦