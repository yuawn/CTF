#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#define N 7

// 放棄ㄅ，這支程式沒有漏洞的>.0
// 現在放棄寒假就開始了

void menu(){
    puts("=====================================");
    puts("Welcome to suuuuuuuper secure RPG - Dragon Slayer!!");
    puts("You can save the world!!!!!");
    // 其實不能
    puts("Please choose what you want to do:");
    puts("1. List characters");
    puts("2. Select character");
    puts("3. Start game");
    puts("87. Exit game");
    puts("=====================================");
}

void game_menu(){
    puts("=====================================");
    puts("GL&HF!!");
    puts("Please choose what you want to do:");
    puts("1. Fight the mighty dragon");
    puts("2. Fight slime");
    puts("3. Craft weapon");
    puts("4. Sleep");
    puts("5. Change name");
    puts("87. Back to menu");
    puts("=====================================");
}

int read_n(char *buf, int n){
    int ret = read(0, buf, n);
    if (ret <= 0){
        puts("read error!");
        exit(-1);
    }
    buf[ret-1] = '\0';
    return ret;
}

long long read_int(){
    char buf[32];
    read_n(buf, 31);
    return atoll(buf);
}

// 名字我想超久der
char *names[N] = {
    "Readdy",
    "OrzanggeOrzangge",
    "Yaloooooooow",
    "Griin",
    "Bulueeeeee",
    "Violeta",
    "Purpling",
};

typedef struct Weapon{
    long long durability;
    char description[128];
    struct Weapon *next;
} Weapon;

typedef struct Character{
    char name[32];
    Weapon *weapons;
    int energy;
    int level;
} Character;

Character *characters;
int changed_name_cnt, dragon_dead;

Weapon* new_weapon(char *name, Weapon *next){
    Weapon *tmp = malloc(sizeof(Weapon));
    sprintf(tmp->description, "%s's weapon", name);
    tmp->durability = 3;
    tmp->next = next;
    return tmp;
}

void init(){
    characters = malloc(sizeof(Character)*N);
    for (int i = 0; i < N; ++i){
        strcpy(characters[i].name, names[i]);
        characters[i].level = 1;
        characters[i].energy = 10;
        characters[i].weapons = new_weapon(names[i], 0);
    }
}

void list_character(){
    for (int i = 0; i < N; ++i){
        puts("-------------------------------------");
        printf("Character %d\n", i);
        printf("Name: %s\n",   characters[i].name);
        printf("Level: %d\n",   characters[i].level);
        printf("Energy: %d\n",   characters[i].energy);
        if (characters[i].weapons)
            printf("Weapon durability: %lld\n", characters[i].weapons->durability);
    }
    puts("-------------------------------------");
}

int out_of_bound(Character *p){
    // if (characters <= p && p <= characters+N) return 0;
    // 差點寫錯ㄏㄏ
    if (characters <= p && p < characters+N) return 0;
    return 1;
}

void fight_dragon(Character *selected){
    if (dragon_dead){
        puts("The Dragon is already dead.");
        return;
    }
    if (selected != &characters[0]){
        // Yo~ 諧音梗
        puts("You can fight the dragon only when you are Readdy!!");
        return;
    }
    if (selected->energy < 10){
        puts("Not enough energy!!");
        return;
    }
    selected->energy -= 10;
    // 反正你練到這ㄍ等級前就timeout了ㄏㄏ
    if (selected->level < 7122222){
        puts("You are killed by the mighty dragon!!");
        puts("So sad...");
        exit(-1);
    }
    dragon_dead = 1;
    puts("You killed the mighty dragon!!!!!!!");
    puts("You got the power to change the world!");
    // people can't have the power to change the world
    long long addr, val;
    printf("Where to change: ");
    addr = read_int();
    printf("What to change: ");
    val = read_int();
    *(long long *)addr = val;
    puts("Thanks for saving the world!!");
}

void fight_slime(Character *selected){
    // 慢慢殺史萊姆升級ㄅ
    if (selected->energy < 1){
        puts("Not enough energy!!");
        return;
    }
    if (selected->weapons == NULL){
        puts("Don't have weapons!!");
        return;
    }
    if (selected->weapons->durability == 1){
        Weapon *tmp = selected->weapons;
        selected->weapons = tmp->next;
        free(tmp);
    } else {
        --selected->weapons->durability;
    }
    --selected->energy;
    ++selected->level;
}

void craft_weapon(Character *selected){
    if (selected->energy < 1){
        puts("Not enough energy!!");
        return;
    }
    selected->weapons = new_weapon("ballon", selected->weapons);
    --selected->energy;
}

void char_sleep(Character *selected){
    // 要睡飽飽才有力氣ㄛ
    sleep(3);
    selected->energy += 10;
}

void change_name(Character *selected){
    char buf[17];
    // 一般遊戲都只給改一次名
    // 這給改兩次
    // 佛心公司
    if (changed_name_cnt < 2){
        printf("New name: ");
        read_n(buf, 17);
        strcpy(selected->name, buf);
        ++changed_name_cnt;
        puts("Name changed!");
        list_character();
    } else {
        puts("Change name limit reached!!");
    }
}

void start_game(Character *selected){
    long long choice;
    while (1){
        game_menu();
        printf("Your choice: ");
        choice = read_int();
        switch (choice){
            case 1:
                fight_dragon(selected);
                break;
            case 2:
                fight_slime(selected);
                break;
            case 3:
                craft_weapon(selected);
                break;
            case 4:
                char_sleep(selected);
                break;
            case 5:
                change_name(selected);
                break;
            case 87:
                return;
        }
    }
}

int main(int argc, char *argv[]){
    long long choice, selected = -1;
    Character *sel;
    alarm(60);
    setvbuf(stdin, NULL, _IONBF, 0); 
    setvbuf(stdout, NULL, _IONBF, 0); 
    init();
    while (1){
        // 不用看了
        // 沒有漏洞的
        // 現在放棄寒假就開始了
        menu();
        printf("Your choice: ");
        choice = read_int();
        switch (choice){
            case 1:
                list_character();
                break;
            case 2:
                printf("Select a character: ");
                selected = read_int();
                if (out_of_bound(&characters[selected])){
                    puts("You can not select this!!");
                    selected = -1;
                    sel = NULL;
                    exit(-1);
                } else {
                    printf("%lld selected\n", selected);
                    sel = &characters[selected];
                }
                break;
            case 3:
                if (selected == -1){
                    puts("You must select a character first!!");
                } else {
                    start_game(sel);
                }
                break;
            case 87:
                exit(0);
                break;
            default:
                puts("Invalid choice!");
        }
    }    
}
