import xml.etree.ElementTree as ET
from xml.dom.minidom import getDOMImplementation

import csv



#
#csvFile = 'myData.csv'
#csvData = csv.reader(open(csvFile))
def main():
    with open(r'\\svm-netapp-dlib.in.library.ucla.edu\DLIngest\gm_rasa_bak\rasainterviews_metadata.csv',
              encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"', doublequote=True )
        for row in reader:
            print(len(row.keys()))
            print(row.keys())
            printxml(row)

def printxml(row):

    impl = getDOMImplementation()
    newdoc = impl.createDocument('http://www.loc.gov/mods/v3', 'mods:mods', None)
    top_element = newdoc.documentElement
    top_element.setAttribute('xmlns:mods', 'http://www.loc.gov/mods/v3')
    top_element.setAttribute('xmlns:xlink', 'http://www.w3.org/1999/xlink')
    top_element.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    top_element.setAttribute('xsi:schemaLocation',
                             'http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-4.xsd')

    # relatedItem Collection Name and Repository name

    elRelatedItem = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:relatedItem')
    eTitleInfoCollectionName = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
    eTitleCollectionName = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
    eTitleCollectionName.appendChild(newdoc.createTextNode('Green Movement collection'))
    eTitleInfoCollectionName.appendChild(eTitleCollectionName)
    elRelatedItem.appendChild(eTitleInfoCollectionName)
    top_element.appendChild(elRelatedItem)
    eNameRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:name')
    eNameRepository.setAttribute('type','corporate')
    eNameRepository.setAttribute('authority','naf')
    eNamePartRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3','mods:namePart')
    eNamePartRepository.appendChild(newdoc.createTextNode('University of California, Los Angeles. $b Library.'))
    eNameRepository.appendChild(eNamePartRepository)
    eNameRoleRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3','mods:role')
    eNameRolTermTextRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3','mods:roleTerm')
    eNameRolTermTextRepository.setAttribute('type','text')
    eNameRolTermTextRepository.appendChild(newdoc.createTextNode('repository'))
    eNameRolTermCodeRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:roleTerm')
    eNameRolTermCodeRepository.setAttribute('type','code')
    eNameRolTermCodeRepository.setAttribute('authority','marcrelator')
    eNameRolTermCodeRepository.appendChild(newdoc.createTextNode('rps'))
    eNameRoleRepository.appendChild(eNameRolTermTextRepository)
    eNameRoleRepository.appendChild(eNameRolTermCodeRepository)
    eNameRepository.appendChild(eNameRoleRepository)
    top_element.appendChild(eNameRepository)



    if 'Title (English)' in row:
        #row['Title (English)']:
        if row['Title (English)']:
            elTitleInfo = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
            eTitle = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
            eTitle.appendChild(newdoc.createTextNode(row['Title (English)']))
            eTitle.setAttribute('lang', 'eng')
            elTitleInfo.appendChild(eTitle)
            top_element.appendChild(elTitleInfo)

    if 'Title (Farsi)' in row:
        #row['Title (Farsi)']:
        if row['Title (Farsi)']:
            elTitleInfoFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
            eTitleFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
            eTitleFarsi.appendChild(newdoc.createTextNode(row['Title (Farsi)']))
            eTitleFarsi.setAttribute('lang', 'per')
            elTitleInfoFarsi.appendChild(eTitleFarsi)
            top_element.appendChild(elTitleInfoFarsi)

    if 'Genre' in row:
        if row['Genre']:
            eGenre = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:genre')
            eGenre.appendChild(newdoc.createTextNode(row['Genre']))
            eGenre.setAttribute('lang', 'eng')
            top_element.appendChild(eGenre)


    if 'Lat, Lon' in row:
        if row['Lat, Lon']:
            eLatLonSubject = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            eLatLonCartographics = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:cartographics')
            eLatLoncoordinates = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:coordinates')
            eLatLoncoordinates.appendChild(newdoc.createTextNode(row['Lat, Lon']))
            eLatLonCartographics.appendChild(eLatLoncoordinates)
            eLatLonSubject.appendChild(eLatLonCartographics)
            top_element.appendChild(eLatLonSubject)

    if 'Physical Type ' in row:
        if row['Physical Type ']:
            ePhysicalDescription = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:physicalDescription')
            eDigitalOrigin = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:digitalOrigin')
            eDigitalOrigin.appendChild(newdoc.createTextNode('born digital'))
            ePhysicalDescription.appendChild(eDigitalOrigin)
            eReformattingQuality = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:reformattingQuality')
            eReformattingQuality.appendChild(newdoc.createTextNode('preservation'))
            ePhysicalDescription.appendChild(eReformattingQuality)
            if 'Video' in row['Physical Type '] or 'video' in row['Physical Type ']:
                eExtent = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:extent')
                eExtent.appendChild(newdoc.createTextNode('moving image'))
                ePhysicalDescription.appendChild(eExtent)
                eInternetMediaType = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:internetMediaType')
                eInternetMediaType.appendChild(newdoc.createTextNode('video/mp4'))
                ePhysicalDescription.appendChild(eInternetMediaType)
                eTypeOfResource = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:typeOfResource')
                eTypeOfResource.appendChild(newdoc.createTextNode('moving image'))
                eGenreVideo = newdoc.createElementNS('http://www.loc.gov/mods/v3','mods:genre')
                eGenreVideo.setAttribute('lang','eng')
                eGenreVideo.appendChild(newdoc.createTextNode('video recordings'))
                top_element.appendChild(eGenreVideo)
                top_element.appendChild(eTypeOfResource)
            elif 'Image' in row['Physical Type '] or 'Photo' in row['Physical Type '] or 'image' in row['Physical Type '] or 'photo' in row['Physical Type ']:
                eExtent = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:extent')
                eExtent.appendChild(newdoc.createTextNode('still image'))
                ePhysicalDescription.appendChild(eExtent)
                eInternetMediaType = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:internetMediaType')
                eInternetMediaType.appendChild(newdoc.createTextNode('image/jpeg'))
                ePhysicalDescription.appendChild(eInternetMediaType)
                eTypeOfResource = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:typeOfResource')
                eTypeOfResource.appendChild(newdoc.createTextNode('still image'))
                top_element.appendChild(eTypeOfResource)
            top_element.appendChild(ePhysicalDescription)

    # <mods:note lang="eng">

    if 'Description (English)' in row:
        if row['Description (English)']:
            eNoteDescription = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
            eNoteDescription.appendChild(newdoc.createTextNode(row['Description (English)']))
            eNoteDescription.setAttribute('lang', 'eng')
            top_element.appendChild(eNoteDescription)

    if 'Description (Farsi)' in row:
        if row['Description (Farsi)']:
            eNoteDescriptionFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
            eNoteDescriptionFarsi.appendChild(newdoc.createTextNode(row['Description (Farsi)']))
            eNoteDescriptionFarsi.setAttribute('lang', 'per')
            top_element.appendChild(eNoteDescriptionFarsi)


    # //<mods:note lang="eng" displayLabel="Names">
    if 'Names (Transliterated)' in row:
        if row['Names (Transliterated)']:
            namesEnglishData = row['Names (Transliterated)'].split('/')
            for data in namesEnglishData:
                eNoteNames = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
                eNoteNames.appendChild(newdoc.createTextNode(data))
                eNoteNames.setAttribute('transliteration', 'unspecified')
                eNoteNames.setAttribute('displayLabel', 'Names')
                top_element.appendChild(eNoteNames)



    #//<mods:note lang="per" displayLabel="Names">
    if 'Names (Farsi)' in row:
        if row['Names (Farsi)']:
            namesFarsiData = row['Names (Farsi)'].split('/')
            for data in namesFarsiData:
                eNoteNamesFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
                eNoteNamesFarsi.appendChild(newdoc.createTextNode(data))
                eNoteNamesFarsi.setAttribute('lang','per')
                eNoteNamesFarsi.setAttribute('displayLabel','Names')
                top_element.appendChild(eNoteNamesFarsi)


    #<mods:note lang="eng" displayLabel="Keywords/Chants/Slogans">
    if 'Keywords/Chants/Slogans (English)' in row:
        if row['Keywords/Chants/Slogans (Farsi)']:
           keywordsData = row['Keywords/Chants/Slogans (English)'].split('/')
           for data in keywordsData:
               eNoteKeywords = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
               eNoteKeywords.appendChild(newdoc.createTextNode(data))
               eNoteKeywords.setAttribute('lang', 'eng')
               eNoteKeywords.setAttribute('displayLabel', 'Keywords/Chants/Slogans')
               top_element.appendChild(eNoteKeywords)

    if 'Keywords/Chants/Slogans (Farsi)' in row:
        if row['Keywords/Chants/Slogans (Farsi)']:
            keywordFarsiData = row['Keywords/Chants/Slogans (Farsi)'].split('/')
            for data in keywordFarsiData:
                eNoteKeywordsFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
                eNoteKeywordsFarsi.appendChild(newdoc.createTextNode(data))
                eNoteKeywordsFarsi.setAttribute('lang', 'per')
                eNoteKeywordsFarsi.setAttribute('displayLabel', 'Keywords/Chants/Slogans')
                top_element.appendChild(eNoteKeywordsFarsi)




    #<mods:subject><mods:hierarchicalGeographic><mods:country lang="eng">
    if 'Country (English)' in row:
        if row['Country (English)']:
            eCountrySubject = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            eCountryHierarchicalGeographic = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:hierarchicalGeographic')
            ecountry = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:country')
            ecountry.appendChild(newdoc.createTextNode(row['Country (English)']))
            ecountry.setAttribute('lang','eng')
            eCountryHierarchicalGeographic.appendChild(ecountry)
            eCountrySubject.appendChild(eCountryHierarchicalGeographic)
            top_element.appendChild(eCountrySubject)

    if 'Country (Farsi)' in row:
        if row['Country (Farsi)']:
            eCountrySubjectFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            eCountryHierarchicalGeographicFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3',
                                                                    'mods:hierarchicalGeographic')
            ecountryFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:country')
            ecountryFarsi.appendChild(newdoc.createTextNode(row['Country (Farsi)']))
            ecountryFarsi.setAttribute('lang', 'per')
            eCountryHierarchicalGeographicFarsi.appendChild(ecountryFarsi)
            eCountrySubjectFarsi.appendChild(eCountryHierarchicalGeographicFarsi)
            top_element.appendChild(eCountrySubjectFarsi)

     #//<mods:subject><mods:hierarchicalGeographic><mods:city lang="eng">

    if 'City (LCSH or Transliterated)' in row:
        if row['City (LCSH or Transliterated)']:
            ecitySubject = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            ecityHierarchicalGeographic = newdoc.createElementNS('http://www.loc.gov/mods/v3',
                                                                    'mods:hierarchicalGeographic')
            ecity = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:city')
            ecity.appendChild(newdoc.createTextNode(row['City (LCSH or Transliterated)']))
            ecity.setAttribute('transliteration', 'unspecified')
            ecityHierarchicalGeographic.appendChild(ecity)
            ecitySubject.appendChild(ecityHierarchicalGeographic)
            top_element.appendChild(ecitySubject)

    if 'City (Farsi)' in row:
        if row['City (Farsi)']:
            ecitySubjectFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            ecityHierarchicalGeographicFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3',
                                                                         'mods:hierarchicalGeographic')
            ecityFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:city')
            ecityFarsi.appendChild(newdoc.createTextNode(row['City (Farsi)']))
            ecityFarsi.setAttribute('lang', 'per')
            ecityHierarchicalGeographicFarsi.appendChild(ecityFarsi)
            ecitySubjectFarsi.appendChild(ecityHierarchicalGeographicFarsi)
            top_element.appendChild(ecitySubjectFarsi)

    eOriginInfo = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
    if 'Date (Normalized)' in row:
        if row['Date (Normalized)']:
            #eOriginInfoDateNormalized = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
            eDateCreatedNormalized = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:dateCreated')
            eDateCreatedNormalized.appendChild(newdoc.createTextNode(row['Date (Normalized)']))
            eDateCreatedNormalized.setAttribute('encoding','iso8601')
            eOriginInfo.appendChild(eDateCreatedNormalized)
            top_element.appendChild(eOriginInfo)

    if 'Date (Gregorian)' in row:
        if row['Date (Gregorian)']:
            #eOriginInfoDateGregorian = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
            eDateCreatedGregorian = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:dateCreated')
            eDateCreatedGregorian.appendChild(newdoc.createTextNode(row['Date (Gregorian)']))
            eDateCreatedGregorian.setAttribute('lang', 'eng')
            eOriginInfo.appendChild(eDateCreatedGregorian)
            top_element.appendChild(eOriginInfo)

    if 'Date (Farsi)' in row:
        if row['Date (Farsi)']:
            #eOriginInfoDateFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
            eDateCreatedFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:dateCreated')
            eDateCreatedFarsi.appendChild(newdoc.createTextNode(row['Date (Farsi)']))
            eDateCreatedFarsi.setAttribute('lang', 'per')
            eOriginInfo.appendChild(eDateCreatedFarsi)
            top_element.appendChild(eOriginInfo)

    #mods:identifier type=local
    if 'file name (no extension indicates folder name)' in row:
        if row['file name (no extension indicates folder name)']:
            eidentifier = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:identifier')
            eidentifier.appendChild(newdoc.createTextNode(row['file name (no extension indicates folder name)']))
            eidentifier.setAttribute('type', 'local')
            top_element.appendChild(eidentifier)
            with open(r'\\svm-netapp-dlib.in.library.ucla.edu\DLIngest\gm_rasa_bak\mods\{}.xml'.format(row['file name (no extension indicates folder name)']), 'w', encoding='utf-8') as f:
                f.write(newdoc.toprettyxml())
    elif 'Filename' in row:
        if row['Filename']:
            eidentifier = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:identifier')
            eidentifier.appendChild(newdoc.createTextNode(row['Filename']))
            eidentifier.setAttribute('type', 'local')
            top_element.appendChild(eidentifier)
            with open(r'\\svm-netapp-dlib.in.library.ucla.edu\DLIngest\gm_rasa_bak\mods\{}.xml'.format(row['Filename']), 'w', encoding='utf-8') as f:
                f.write(newdoc.toprettyxml())



    print(newdoc.toprettyxml())





if __name__ == '__main__': main()

