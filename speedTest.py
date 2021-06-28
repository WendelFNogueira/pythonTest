import speedtest


def test():
    test = speedtest.Speedtest()
    test.get_servers()
    test.get_best_server()
    test.download()
    test.upload()
    resultado = test.results.dict()
    return resultado["download"], resultado["upload"], resultado["ping"]


def main():
    # write to csv
    with open('file.csv', 'w') as file:
        file.write('download,upload,ping\n')
        for i in range(3):
            print('Making test #{}'.format(i+1))
            download, upload, ping = test()
            file.write('{},{},{}\n'.format(download, upload, ping))
    # pretty write to txt file
    with open('file.txt', 'w') as file:
        for i in range(3):
            print('Making test #{}'.format(i+1))
            download, upload, ping = test()
            file.write('Test #{}\n'.format(i+1))
            file.write('Download: {:.2f} Kb/s\n'.format(download / 1024))
            file.write('Upload: {:.2f} Kb/s\n'.format(upload / 1024))
            file.write('Ping: {}\n'.format(ping))
    # simply print in needed format if you want to use pipe-style: python script.py > file
    for i in range(3):
        download, upload, ping = test()
        print('Test #{}\n'.format(i+1))
        print('Download: {:.2f} Kb/s\n'.format(download / 1024))
        print('Upload: {:.2f} Kb/s\n'.format(upload / 1024))
        print('Ping: {}\n'.format(ping))


if __name__ == '__main__':
    main()