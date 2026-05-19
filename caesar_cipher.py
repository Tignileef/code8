def decode_character(char, shift):
    # 알파벳의 대소문자 기준값을 각각 다르게 설정한다.
    if 'a' <= char <= 'z':
        base_code = ord('a')
    elif 'A' <= char <= 'Z':
        base_code = ord('A')
    else:
        # 알파벳이 아닌 문자는 공백, 기호 등을 유지하기 위해 그대로 반환한다.
        return char

    # 현재 알파벳 위치에 자리수를 더하고, 26으로 나눈 나머지로 순환시킨다.
    char_code = ord(char) - base_code
    decoded_code = (char_code + shift) % 26 + base_code

    return chr(decoded_code)


def caesar_cipher_decode(target_text):
    # 보너스 과제용 사전이다. 해독 결과에 단어가 있으면 추천 자리수로 표시한다.
    dictionary = ['love', 'mars', 'key', 'door', 'password']
    decoded_results = []
    recommended_shift = None

    # 알파벳 개수만큼 0부터 25까지 모든 자리수를 시도한다.
    for shift in range(26):
        decoded_text = ''

        # 입력받은 문자열을 한 글자씩 카이사르 암호 방식으로 해독한다.
        for char in target_text:
            decoded_text += decode_character(char, shift)

        # 자리수별 해독 결과를 저장하고 화면에 출력한다.
        decoded_results.append(decoded_text)
        print(str(shift) + ': ' + decoded_text)

        # 사전에 있는 단어가 발견되면 해당 자리수를 추천값으로 저장한다.
        lower_text = decoded_text.lower()
        if recommended_shift is None:
            for word in dictionary:
                if word in lower_text:
                    recommended_shift = shift
                    break

    return decoded_results, recommended_shift


def read_password(file_name):
    # password.txt 파일을 읽어오며, 파일 처리 오류는 예외처리한다.
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(file_name + ' was not found.')
    except OSError as error:
        print('File read error: ' + str(error))

    return None


def save_result(file_name, result_text):
    # 선택한 최종 해독 결과를 result.txt 파일로 저장한다.
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(result_text)
        print('Saved decoded text to ' + file_name + '.')
    except OSError as error:
        print('File write error: ' + str(error))


def get_shift_number(recommended_shift):
    # 사전 단어로 찾은 추천 자리수가 있으면 먼저 출력한다.
    if recommended_shift is not None:
        print('Recommended shift: ' + str(recommended_shift))

    # 사용자가 올바른 자리수 번호를 입력할 때까지 반복한다.
    while True:
        user_input = input('Enter decoded shift number: ')

        try:
            shift_number = int(user_input)
        except ValueError:
            print('Please enter a number from 0 to 25.')
            continue

        if 0 <= shift_number < 26:
            return shift_number

        print('Please enter a number from 0 to 25.')


def main():
    # 암호문을 파일에서 읽고, 해독 결과를 확인한 뒤 최종 결과를 저장한다.
    target_text = read_password('password.txt')

    if target_text is None:
        return

    decoded_results, recommended_shift = caesar_cipher_decode(target_text)
    shift_number = get_shift_number(recommended_shift)
    save_result('result.txt', decoded_results[shift_number])


if __name__ == '__main__':
    main()
