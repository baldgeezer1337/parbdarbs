import json
from datetime import datetime

apmekletaji=[]
def load_data():     
    file=open('apmekletaji.json', 'r')
    data=json.load(file)
    file.close()
    global apmekletaji
    apmekletaji=data['apmekletaji']
    print('Dati loaded')

now = datetime.now()

def add_apmekletajs():
    apmekletajs_name=input('Apmekletajs name: ')
    apmekletajs_pilseta=input('Apmekletajs pilseta: ')
    apmekletajs_id=input('Apmekletajs id: ')
    apmekletajs_talrunis=input('Apmekletajs talrunis: ')

    apmekletajs={
            'name':apmekletajs_name,
            'pilseta':apmekletajs_pilseta,
            'id': apmekletajs_id,
            'talrunis': apmekletajs_talrunis,
             'apmeklejums': []
         }  
    while (True):
        response=input('Vai velaties pieteikties apmeklejumam? (y/n)')
        if response=='y':
                apmeklejums_time=input('Cik ilgs apmeklejums: ')
                apmeklejums_berni=input('Cik daudz bernu: ')
                apmeklejums_datums=input('Datums: ')
                apmeklejums_udens=input('Dzerama udens iegāde (1 udens=0,45$): ')


                info={
                    'time': apmeklejums_time,
                    'berni': apmeklejums_berni,
                    'datums':apmeklejums_datums,
                    'udens':apmeklejums_udens
                }
                apmekletajs['apmeklejums'].append(info)
                print('Apmeklejums ir izveidots: ',now)
        elif response=='n':
            break
    apmekletaji.append(apmekletajs)
def print_apmekletajs():
             for apmekletajs in apmekletaji:
                print('---Apmekletajs---')
                print(f"Apmekletaja vards: {apmekletajs['name']}({apmekletajs['id']})")
                print(f"Pilseta:{apmekletajs['pilseta']}")
                print(f"Kontaktu skaits:{len(apmekletajs['apmeklejums'])}")

def save_data():
    data={
         'apmekletaji':apmekletaji
     }
    print('Saving data...')
    file=open('apmekletaji.json', 'w')
    json.dump(data,file, indent=4)
    print('Data saved')

def find_person_by_id():
    apmekletajs_id=input('Ievadiet cilveka ID, lai atrast kontaktpersonu: ').strip()
    for apmekletajs in apmekletaji:
              if apmekletajs['id']==apmekletajs_id:
                   print(f"Kontakts ir {apmekletajs}")
                   return
    print('Cilveks ar noraidito ID netika atrasts.')

def main():
    #load_data()
    #add_apmekletajs()
   # print_apmekletajs()
    #save_data()
    #find_person_by_id()
    while (True):
        response=input('(1) Pievienot Apmekletaju (2) Paradit apmeklejumus (3)Atrast apmekletaju ar ID (4)Saglabat datus (5) Exit')
        if response=='1':
            add_apmekletajs()         
        elif response=='2':
            print_apmekletajs()
        elif response=='3':
            find_person_by_id()
        elif response=='4':
            save_data()
        elif response=='5':
            save_data()
            print('Bye bye!')
            exit()
        else:
            print('Choose a number between 1-4')
            continue
main()
