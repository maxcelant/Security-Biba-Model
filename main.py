from subject_class import Subject
from object_class import Object
from referencemonitor import ReferenceMonitor

refMon = ReferenceMonitor()  # create global reference monitor object


def validate_exchange(data):
    command = data.split(' ')

    if len(command) != 4:
        print('Bad Instruction : ' + data)
        return

    exhange_type, subject_name, object_name, amount = command

    # try to turn amount to float
    try:
        amount = float(amount)
    except ValueError:
        print('Bad Instruction : ' + data)
        return

    refMon.execute_exchange(exhange_type, subject_name, object_name, amount)


def validate_query(data):
    command = data.split(' ')

    if len(command) != 3:
        print('Bad Instruction : ' + data)
        return

    _, subject_name, object_name = command

    # attempt to find obj & subject and execute query
    refMon.execute_query(subject_name, object_name)


def validate_add(data):

    security_levels = ('LOW', 'MEDIUM', 'HIGH')

    command = data.split(' ')

    if len(command) != 3:  # validate if 3 strings were entered
        print('Bad Instruction : ' + data)
        return

    add_type, name, security_level = command

    if len(name) > 20 or len(name) < 1:  # check name length
        print('Bad Instruction : ' + data)
        return

    if security_level.upper() not in security_levels:  # validate security level
        print('Bad Instruction : ' + data)
        return

    add_to_referencemonitor(add_type, name, security_level)


# after validation, add the subject/object to the reference monitor
def add_to_referencemonitor(add_type, name, security_level):
    if add_type.lower() == 'addsub':
        subject = Subject(name)
        refMon.add_subject(subject, security_level)
    elif add_type.lower() == 'addobj':
        obj = Object(name)
        refMon.add_object(obj, security_level)


def main():
    while True:
        cli_input = input()
        # check if user is trying to add an subject/object
        if cli_input[:6].lower() == 'addsub' or cli_input[:6].lower() == 'addobj':
            validate_add(cli_input)

        # check if user is trying to query
        elif cli_input[:5].lower() == 'query':
            validate_query(cli_input)

        # check if user wants to see status
        elif cli_input.lower() == 'status':
            refMon.print_status()

        # check if user wants to make a deposit or withdraw
        elif cli_input[:7].lower() == 'deposit' or cli_input[:8].lower() == 'withdraw':
            validate_exchange(cli_input)

        else:
            print('Bad Instruction : ' + cli_input)


if __name__ == '__main__':
    main()
