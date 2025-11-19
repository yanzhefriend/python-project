###统计文件的字数，行数，非空行数，字符数
class Filestats:
    def __init__(self,filename):
        self.filename=filename
        #初始化统计性信息
        self.lines_count=0
        self.non_empty_lines_count = 0
        self.words_count = 0
        self.char_count = 0
        self.file_found=True
        self._read_file()

    def _read_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    self.lines_count+= 1
                    if line.strip():
                        self.non_empty_lines_count+=1
                    self.words_count+=len(line.split())
                    self.char_count+=len(line)
        except FileNotFoundError:
            self.file_found = False

    def lines(self):
        if not self.file_found:  #相当于"if self.file_found==False"
            return"File not found, please check if the file's name is correct"
        return f"This file has {self.lines_count} line{''if self.lines_count==1 else 's'}"
        #因为return会立刻退出函数，所以不需要“else："

    def non_empty_lines(self):
        if not self.file_found:
            return "File not found, please check if the file's name is correct"
        return f"This file has {self.non_empty_lines_count} non-empty line{'' if self.non_empty_lines_count == 1 else 's'}"

    def words(self):
        if not self.file_found:
            return "File not found, please check if the file's name is correct"
        return f"This file has {self.words_count} word{'' if self.words_count == 1 else 's'}"

    def char(self):
        if not self.file_found:
            return "File not found, please check if the file's name is correct"
        return f"This file has {self.char_count} character{'' if self.char_count == 1 else 's'}"

file1 = input("Tell me the file's name:")
stats=Filestats(file1)

print(stats.lines())
print(stats.non_empty_lines())
print(stats.words())
print(stats.char())