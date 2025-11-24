from models.member import Member

filename = "data/members.txt"
all_members = []

def load_members():
    all_members.clear()
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                m = Member(parts[0], parts[1], parts[2])
                
                if parts[3] != "None":
                    m.borrowed_books = parts[3].split("|")
                
                all_members.append(m)
                
    except FileNotFoundError:
        print("Member file not found. No members yet.")

def save_members():
    f = open(filename, "w")
    for m in all_members:
        f.write(str(m) + "\n")
    f.close()

def add_new_member(m_id, name, email):
    new_m = Member(m_id, name, email)
    all_members.append(new_m)
    save_members()
    print(">> Success: Member registered!")

def get_member_by_id(m_id):
    for m in all_members:
        if m.member_id == m_id:
            return m
    return None