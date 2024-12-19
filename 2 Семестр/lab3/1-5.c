#include <stdlib.h>
#include <stdio.h>

struct ListNode
{
    struct ListNode *pre;
    struct ListNode *next;
    int value;
};

int main(void)
{
    // Начало списка
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    // Конец списка
    struct ListNode *tail = head;

    // Заполняем список значениями от 0 до 10
    for (int i = 1; i < 10; i++)
    {
        struct ListNode *new_node = (struct ListNode *)malloc(sizeof(struct ListNode));
        // Новое значение
        new_node->value = i;
        // Указываем предыдущий элемент
        new_node->pre = tail;
        // Т.к. этот элемент последний, сл. элемент равен нулю
        new_node->next = NULL;
        // Обновняем указатель предыдущего элемента
        tail->next = new_node;
        // Обновляем конец списка
        tail = new_node;
    }
    // Выводим значения списка
    struct ListNode *node = head;
    while (node != NULL)
    {
        printf("%d -> ", node->value);
        node = node->next;
    }
    printf("NULL\n");
    // Выводим значения списка в обратном порядке
    node = tail;
    while (node != NULL)
    {
        printf("%d <- ", node->value);
        node = node->pre;
    }
    printf("NULL\n");

    return 0;
}