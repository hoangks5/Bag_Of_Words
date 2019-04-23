'''Các công đoạn
    1. Tách từ trong câu, dùng thư viện underthesea để tách từ tiếng việt
       https://github.com/undertheseanlp/word_tokenize, độ chính xác 97.65%
    2. Chuyển các từ về dạng viết thường hết
#     3. Loại bỏ các từ không có ý nghĩa. Dùng file stopword
#         https://github.com/stopwords/vietnamese-stopwords
#     4. Đếm số lần xuất hiện của các từ còn lại
# '''
#
# import re
# # Dùng để tách từ tiếng việt #vietnamese NLP toolkit
from underthesea import word_tokenize
from collections import Counter
# Dùng để đọc file utf8
import codecs

# Đọc file chứa những từ không mang ý nghĩa trong tiếng việt
filename = "stopword.txt"
# Đọc file và lưu thành mảng
with codecs.open(filename, 'r', encoding='utf8') as f_obj:
    stopwords = [line.rstrip('\r\n') for line in f_obj]

if __name__ == "__main__":
    print("Nhập vào văn bản cần xét:")
    text = input()
    # Chuyển đầu vào thành viết thường hết
    text_lower = text.lower()
    # Tách các từ và cụm từ
    #[^\r]: Loại bỏ các kí tự không phải chữ, số và dấu gạch dưới
    text_clear = re.sub(r'[^\w]', ' ', text_lower)
    word_tokenize = word_tokenize(text_lower)

    # Chuyển list thành 1 dict. Với key là phần tử trong list và value là số lần xuất hiện của phần tử đó trong list
    # Trả về danh sách các phần tử được sắp xếp theo độ phổ biến giảm dần
    counter = Counter(word_tokenize).most_common()
    print("===============================\nSố lần xuất hiện của các từ là:")
    for item in counter:
        #kiểm tra nếu có trong stopword thì loại bỏ
        print(item[0])
        if item[0] in stopwords:
            continue
        else:
            print("{}: {}".format(item[0],item[1]))