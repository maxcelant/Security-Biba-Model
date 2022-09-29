class ReferenceMonitor:
    
    def __init__(self):
        self.object_levels = {'HIGH': [], 'MEDIUM': [], 'LOW': []}
        self.subject_levels = {'HIGH': [], 'MEDIUM': [], 'LOW': []}
        self.integrity_levels = {'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}
    
    
    # add a object to correct integrity group
    def add_object(self, obj, security_level):
        self.object_levels[security_level.upper()].append(obj)
        print('Object Added : ' + f'addobj {obj.name} {security_level}')
    
    
    # add a subject to correct integrity group
    def add_subject(self, subject, security_level):
        self.subject_levels[security_level.upper()].append(subject)
        print('Subject Added : ' + f'addsub {subject.name} {security_level}')
    
    
    # finds the subject and object, performs query
    def execute_query(self, subject_name, object_name):
        s, o = None, None
        subject_level, object_level = None, None
        # searches through lists for subject with correct subject name
        for integrity_level, subjects in self.subject_levels.items(): 
            for subject in subjects:
                if subject_name == subject.name:
                    s = subject
                    subject_level = integrity_level
                    break
        
        if s is None:
            print('Bad Instruction: Subject not found')
            return
        
        # searches through lists for object with correct object name
        for integrity_level, objects in self.object_levels.items():
            for obj in objects:
                if object_name == obj.name:
                    o = obj
                    object_level = integrity_level
                    break
        
        if o is None:
            print('Bad Instruction: Object not found')
            return
        
        # 'No read down' -> S can read o if i(o) >= i(s)
        # hence, if o < s, then it cannot be done
        if self.integrity_levels[object_level] < self.integrity_levels[subject_level]:
            print('Access Denied: Integrity of Object lower than Subject')
            return
        
        # save current object balance to subject
        s.balance = o.balance
        
        print('Access Granted:' + f' query {s.name} {o.name}')
    
    
    def execute_exchange(self, exchange_type, subject_name, object_name, amount):
        s, o = None, None
        subject_level, object_level = None, None
        # searches through lists for subject with correct subject name
        for integrity_level, subjects in self.subject_levels.items(): 
            for subject in subjects:
                if subject_name == subject.name:
                    s = subject
                    subject_level = integrity_level
                    break
        
        if s is None:
            print('Bad Instruction: Subject not found')
            return
        
        # searches through lists for object with correct object name
        for integrity_level, objects in self.object_levels.items():
            for obj in objects:
                if object_name == obj.name:
                    o = obj
                    object_level = integrity_level
                    break
        
        if o is None:
            print('Bad Instruction: Object not found')
            return
        
        # 'No Write Up' -> s can modify o if i(s) >= i(o)
        # hence if the integrity of s is less than the object, no good
        if self.integrity_levels[subject_level] < self.integrity_levels[object_level]:
            print('Access Denied: Integrity of Subject lower than Object')
            return
        
        # check if its a deposit or withdrawl
        if exchange_type == 'deposit':
            o.balance += amount
            print('Access Granted:' + f' deposit {s.name} {o.name} {amount}')
        else:
            o.balance -= amount
            print('Access Granted:' + f' withdraw {s.name} {o.name} {amount}')
        
          
    
        
    def print_objects(self):
        print(self.object_levels)
    
    
    def print_subjects(self):
        print(self.subject_levels)
    
    
    # prints the current object and subjects 
    def print_status(self):
        print('----------------------------------------------------------------')
        print('                      Current State')
        print('----------------------------------------------------------------')
        print('                         Subjects')
        for key, subjects in self.subject_levels.items():
            for subject in subjects:
                print(f"-> Name: '{subject.name}' Level: '{key}' Balance: '{subject.balance}'")
        print('----------------------------------------------------------------')
        print('                         Objects')
        for key, objects in self.object_levels.items():
            for obj in objects:
                print(f"-> Name: '{obj.name}' Level: '{key}' Balance: '{obj.balance}'")
