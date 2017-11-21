from datetime import datetime
import matcher.fp_matcher as FpMatcher

if __name__ == '__main__':
    startTime = datetime.now()

    fpMatcher = FpMatcher.FpMatcher()
    mainImg = '6'
    inputImg = '4'
    for i in range(1, 5):
        s = '' + str(i)
        fpMatcher.match('./asset/' + mainImg + '_1.BMP',
                        './asset/' + inputImg + '_' + s +'.BMP')

    print(datetime.now() - startTime)