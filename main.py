import argparse


def create_block(args):
    # Логика создания нового блока
    print("Создание нового блока")


def send_transaction(args):
    # Логика отправки транзакции
    print("Отправка транзакции")


def get_block_info(args):
    # Логика получения информации о блоке
    print("Получение информации о блоке")


def main():
    parser = argparse.ArgumentParser(description='CLI для блокчейна Greenfield')

    subparsers = parser.add_subparsers(title='Команды', dest='command')

    # Команда для создания нового блока
    create_block_parser = subparsers.add_parser('create_block', help='Создать новый блок')

    # Команда для отправки транзакции
    send_transaction_parser = subparsers.add_parser('send_transaction', help='Отправить транзакцию')

    # Команда для получения информации о блоке
    get_block_info_parser = subparsers.add_parser('get_block_info', help='Получить информацию о блоке')
    get_block_info_parser.add_argument('block_id', type=int, help='Идентификатор блока')

    args = parser.parse_args()

    if args.command == 'create_block':
        create_block(args)
    elif args.command == 'send_transaction':
        send_transaction(args)
    elif args.command == 'get_block_info':
        get_block_info(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
