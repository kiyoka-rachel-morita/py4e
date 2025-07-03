# Simple reference maker for APU students 
print('APA Style Reference Generator (Book/Online Material/Journal Article/No Author/Encyclopedia/Professional Website/Newspaper Article/Government Report/Foreign Article/Motion Picture)')
print('-----------------------------------------------------')

# Book
ref_type=input('What reference type? (Book/Online Material): ').lower()
if ref_type=='Book':
    author=input('Author (Last, First Initial): ')
    year=input('Year of publication: ')
    title=input('Book title: ')
    publisher=input('Publisher: ')
    print('-----------------------------------------------------')
    print(f'{author} ({year}). *{title}*. {publisher}.')

# Online Material
elif ref_type=='Online Material':
    author=input('Author (Last, First initial): ')
    date=input('Year of publication: ')
    title=input('Article title: ')
    periodical=input('Periodical title: ')
    volume=input('Volume number (If available): ')
    retrieved=input('Retrieved date (e.g., May 5th, 2025): ')
    url=input('URL link: ')
    print('-----------------------------------------------------')
    print(f'{author} ({date}). {title}. *{periodical}*, *{volume}*. Retrieved {retrieved} from {url}')

# Journal Article
elif ref_type=='Journal Article':
    author=input('Author (Last, First initial): ')
    year=input('Year of publication: ')
    title=input('Article title: ')
    periodical=input('Periodical title: ')
    volume=input('Volume number: ')
    issue=input('Issue number (If available): ')
    page=input('Page range:' )
    print('-----------------------------------------------------')
    print(f'{author} {(year)}. {title}. *{periodical}*, *{volume}* ({issue}), {page}.')

# Encyclopedia
elif ref_type=='Encyclopedia':
    title=input('Article title: ')
    date=input('Date of publication (if no date, n.d.): ')
    encyclopedia=input('Name of the encyclepedia: ')
    url=input('URL: ')
    print('-----------------------------------------------------')
    print(f'{title}. ({date}). In {encyclopedia}. Retrieved from {url}')

# No Author
elif ref_type=='No Author':
    title=input('Article title: ')
    date=input('Date on website: ')
    website=input('Website title: ')
    re_date=input('Retrieved date: ')
    url=input('URL: ')
    print('-----------------------------------------------------')
    print(f'{title}. ({date}). {website}. Retrieved {re_date} from {url}')

# Professional Website
elif ref_type=='Professional Website':
    org_name=input('Name of organization: ')
    year=input('Year of publication: ')
    title=input('Page title: ')
    re_date=input('Retrieved date: ')
    url=input('URL: ')
    print('-----------------------------------------------------')
    print(f'{org_name}. ({year}). {title}. Retrieved {re_date} from {url}')

# Newspaper Article
elif ref_type=='Newspaper Article':
    title=input('Article title: ')
    year=input('Year (or full date) of publication: ')
    news_name=input('Name of newspaper: ')
    re_date=input('Retrieved date: ')
    url=input('URL: ')
    print('-----------------------------------------------------')
    print(f'{title}. ({year}). {news_name}. Retrieved {re_date} from {url}')

# Motion Picture
elif ref_type=='Motion Picture':
    pd_name=input("Producer's name: ")
    dr_name=input("Director's name(s): ")
    year=input('Year of release: ')
    title=input('Movie title: ')
    place=input('Place of production: ')
    publisher=input('Publisher/Studio name: ')
    print('---------------------------------------------------------')
    print(f'{pd_name}. (Producer). {dr_name}. (Director). ({year}). {title} [Motion Picture]. {place}: {publisher}')

# Government Report (Online)
elif ref_type=='Government Report':
    entity=input('Name of Government entity: ')
    year=input('Year of publication: ')
    title=input('Report title: ')
    pb_num=input('Publication number: ')
    url=input('URL: ')
    print('--------------------------------------------------------')
    print(f'{entity}.({year}). {title}. ({pb_num}). Retrieved from {url}')

# Foreign Article
elif ref_type=='Foreign Article':
    surname=input("Author's surname: ")
    first_name=input("Author's first name: ")
    year=input('Year of publication: ')
    title_original=input('Title in original language: ')
    title_translated=input('English translation of the title: ')
    url=input('URL: ')
    print('--------------------------------------------------------')
    print(f'{surname}, {first_name}. ({year}). {title_original}. ({title_translated}). Retrieved from {url} ')


