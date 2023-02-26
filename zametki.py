import os

def main():
    # Чтение заметок
    notes = []
    notesList = open(os.getcwd() + '\\notes.txt', 'r').readlines()
    
    # Читаем строки в массив заметок
    for note in notesList:
        if (note.strip(' \t\n\r') != ''): # Проверка на пустые строки
            notes.append(note.strip(' \t\n\r'))
    
    # Сохранение заметок в файл
    def Savenotes():
        file = open('notes.txt', 'w')
        for note in notes:
            file.write(note + "\n");
        file.close()
     
    # Цикл обработки команд
    while True:
        os.system('cls') # Стираем вывод
        
        print('========= Заметки ===========')

        # Выводим
        for i in range(0, len(notes)):
            print(str(i + 1) + '.', notes[i].strip(' \t\n\r'))
        
        print('')
        
        # Спрашиваем пользователя
        qu = input('Добавить заметку? (y/n): ')
        
        if (qu == 'y'):
            note = input('Введите текст: ')
            notes.append(note)
            Savenotes()
            print('Заметка добавлена')
        
        print('')
        
        # Спрашиваем пользователя
        qu = input('Изменить заметку? (y/n): ')
        
        if (qu == 'y'):
            noteID = input('Введите номер заметки: ')
            if (noteID.isdigit() and int(noteID) - 1 < len(notes)):
                note = input('Введите текст: ')
                notes[int(noteID) - 1] = note;
                Savenotes()
                print('Заметка обновлена')
            else:
                print('Неверный номер')
        
        print('')

        qu = input('Найти заметку по ID? (y/n): ')

        if (qu == 'y'):
            noteID = input('Введите номер заметки: ')
            if (noteID.isdigit() and int(noteID) - 1 < len(notes)):
                print(note)
            else:
                print('Неверный номер')
        
        print('')        
        
        # Спрашиваем пользователя
        qu = input('Удалить заметку? (y/n): ')
        
        if (qu == 'y'):
            noteID = input('Введите номер заметки: ')
            if (noteID.isdigit() and int(noteID) - 1 < len(notes)):
                notes.remove(notes[int(noteID) - 1])
                Savenotes()
            else:
                print('Неверный номер')
            
    qu = input('')
    

if __name__=='__main__':
	main()
