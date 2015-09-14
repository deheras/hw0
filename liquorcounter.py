def main():

    file=open("iowa-liquor-sample.csv","r+")

    count=0

    for record in file.readlines():

        record = record.strip()
        found = False

        for value in record.split(","):
            if value.lower() == 'single malt scotch':
                found = True

        if found is True:
            count += 1

    return count

    file.close();


if __name__ == '__main__':
    
    total = main()

    print (total)

