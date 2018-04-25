import xml.etree.ElementTree as ET
from xml.dom.minidom import getDOMImplementation

import csv



# gm_videos3,rasa_tv
#csvFile = 'myData.csv'
#csvData = csv.reader(open(csvFile))
def main():
    with open(r'\\svm-netapp-dlib.in.library.ucla.edu\DLIngest\gm_rasatv1\gm_rasatv1_metadata.csv',
              encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"', doublequote=True)
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
    top_element.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMSchema-instance')
    top_element.setAttribute('xsi:schemaLocation',
                             'http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-4.xsd')
#    print(row['filename'], row['Genre (English)'])

    # relatedItem Collection Name and Repository name

    elRelatedItem = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:relatedItem')
    eTitleInfoCollectionName = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
    eTitleCollectionName = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
    eTitleCollectionName.appendChild(newdoc.createTextNode('Green Movement collection'))
    eTitleInfoCollectionName.appendChild(eTitleCollectionName)
    elRelatedItem.appendChild(eTitleInfoCollectionName)
    top_element.appendChild(elRelatedItem)
    eNameRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:name')
    eNameRepository.setAttribute('type', 'corporate')
    eNameRepository.setAttribute('authority', 'naf')
    eNamePartRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:namePart')
    eNamePartRepository.appendChild(newdoc.createTextNode('University of California, Los Angeles. $b Library.'))
    eNameRepository.appendChild(eNamePartRepository)
    eNameRoleRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:role')
    eNameRolTermTextRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:roleTerm')
    eNameRolTermTextRepository.setAttribute('type', 'text')
    eNameRolTermTextRepository.appendChild(newdoc.createTextNode('repository'))
    eNameRolTermCodeRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:roleTerm')
    eNameRolTermCodeRepository.setAttribute('type', 'code')
    eNameRolTermCodeRepository.setAttribute('authority', 'marcrelator')
    eNameRolTermCodeRepository.appendChild(newdoc.createTextNode('rps'))
    eNameRoleRepository.appendChild(eNameRolTermTextRepository)
    eNameRoleRepository.appendChild(eNameRolTermCodeRepository)
    eNameRepository.appendChild(eNameRoleRepository)
    top_element.appendChild(eNameRepository)
    if 'Title (English)' in row:
        if row['Title (English)']:
            elTitleInfo = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
            eTitle = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
            eTitle.appendChild(newdoc.createTextNode(row['Title (English)'].strip()))
            eTitle.setAttribute('lang', 'eng')
            elTitleInfo.appendChild(eTitle)
            top_element.appendChild(elTitleInfo)

    if 'Title (Farsi)' in row:
        if row['Title (Farsi)']:
            elTitleInfoFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
            eTitleFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
            eTitleFarsi.appendChild(newdoc.createTextNode(row['Title (Farsi)'].strip()))
            eTitleFarsi.setAttribute('lang', 'per')
            elTitleInfoFarsi.appendChild(eTitleFarsi)
            top_element.appendChild(elTitleInfoFarsi)

    if 'Genre (English)' in row:
        if row['Genre (English)']:
            genreEnglishData = row['Genre (English)'].split(' / ')
            for data in genreEnglishData:
                eGenre = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:genre')
                eGenre.appendChild(newdoc.createTextNode(data.strip()))
                eGenre.setAttribute('lang', 'eng')
                top_element.appendChild(eGenre)
    if 'Genre (Farsi)' in row:
        if row['Genre (Farsi)']:
            genreFarsiData = row['Genre (Farsi)'].split(' / ')
            for data in genreFarsiData:
                eGenreFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:genre')
                eGenreFarsi.appendChild(newdoc.createTextNode(data.strip()))
                eGenreFarsi.setAttribute('lang', 'per')
                top_element.appendChild(eGenreFarsi)
    if 'Lat, Lon' in row:
        if row['Lat, Lon']:
            eLatLonSubject = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            eLatLonCartographics = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:cartographics')
            eLatLoncoordinates = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:coordinates')
            eLatLoncoordinates.appendChild(newdoc.createTextNode(row['Lat, Lon'].strip()))
            eLatLonCartographics.appendChild(eLatLoncoordinates)
            eLatLonSubject.appendChild(eLatLonCartographics)
            top_element.appendChild(eLatLonSubject)
    if 'Physical Type' in row:
        if row['Physical Type']:
            ePhysicalDescription = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:physicalDescription')
            eDigitalOrigin = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:digitalOrigin')
            eDigitalOrigin.appendChild(newdoc.createTextNode('born digital'))
            ePhysicalDescription.appendChild(eDigitalOrigin)
            eReformattingQuality = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:reformattingQuality')
            eReformattingQuality.appendChild(newdoc.createTextNode('preservation'))
            ePhysicalDescription.appendChild(eReformattingQuality)
            if 'Video' in row['Physical Type'] or 'video' in row['Physical Type'] or 'moving image' in row['Physical Type']:
                eExtent = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:extent')
                eExtent.appendChild(newdoc.createTextNode('moving image'))
                ePhysicalDescription.appendChild(eExtent)
                eInternetMediaType = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:internetMediaType')
                eInternetMediaType.appendChild(newdoc.createTextNode('video/mp4'))
                ePhysicalDescription.appendChild(eInternetMediaType)
                eTypeOfResource = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:typeOfResource')
                eTypeOfResource.appendChild(newdoc.createTextNode('moving image'))
                #eGenreVideo = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:genre')
                #eGenreVideo.setAttribute('lang', 'eng')
                #eGenreVideo.appendChild(newdoc.createTextNode('digital moving image formats'))
                #top_element.appendChild(eGenreVideo)
                top_element.appendChild(eTypeOfResource)
            top_element.appendChild(ePhysicalDescription)

        #<mods:note lang="eng">
    if 'Description (English)' in row:
        if row['Description (English)']:
            eNoteDescription = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
            eNoteDescription.appendChild(newdoc.createTextNode(row['Description (English)'].strip()))
            eNoteDescription.setAttribute('lang', 'eng')
            top_element.appendChild(eNoteDescription)
    if 'Description (Farsi)' in row:
        if row['Description (Farsi)']:
            eNoteDescriptionFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
            eNoteDescriptionFarsi.appendChild(newdoc.createTextNode(row['Description (Farsi)'].strip()))
            eNoteDescriptionFarsi.setAttribute('lang', 'per')
            top_element.appendChild(eNoteDescriptionFarsi)


        # //<mods:note lang="eng" displayLabel="Names">
    if 'Names (English)' in row:
        if row['Names (English)']:
            namesEnglishData = row['Names (English)'].split(' / ')
            for data in namesEnglishData:
                eNoteNames = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
                eNoteNames.appendChild(newdoc.createTextNode(data.strip()))
                eNoteNames.setAttribute('lang', 'eng')
                eNoteNames.setAttribute('displayLabel', 'Names')
                top_element.appendChild(eNoteNames)


        #//<mods:note lang="per" displayLabel="Names">\
    if 'Names (Farsi)' in row:
        if row['Names (Farsi)']:
            namesFarsiData = row['Names (Farsi)'].split(' / ')
            for data in namesFarsiData:
                eNoteNamesFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
                eNoteNamesFarsi.appendChild(newdoc.createTextNode(data.strip()))
                eNoteNamesFarsi.setAttribute('lang','per')
                eNoteNamesFarsi.setAttribute('displayLabel','Names')
                top_element.appendChild(eNoteNamesFarsi)

        #<mods:note lang="eng" displayLabel="Keywords/Chants/Slogans">
    if 'Keywords/Chants/Slogans (English)' in row:
        if row['Keywords/Chants/Slogans (English)']:
            keywordsData = row['Keywords/Chants/Slogans (English)'].split(' / ')
            for data in keywordsData:
                eNoteKeywords = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
                eNoteKeywords.appendChild(newdoc.createTextNode(data.strip()))
                eNoteKeywords.setAttribute('lang', 'eng')
                eNoteKeywords.setAttribute('displayLabel', 'Keywords/Chants/Slogans')
                top_element.appendChild(eNoteKeywords)

    if 'Keywords/Chants/Slogans (Farsi)' in row:
        if row['Keywords/Chants/Slogans (Farsi)']:
            keywordFarsiData = row['Keywords/Chants/Slogans (Farsi)'].split(' / ')
            for data in keywordFarsiData:
                eNoteKeywordsFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
                eNoteKeywordsFarsi.appendChild(newdoc.createTextNode(data.strip()))
                eNoteKeywordsFarsi.setAttribute('lang', 'per')
                eNoteKeywordsFarsi.setAttribute('displayLabel', 'Keywords/Chants/Slogans')
                top_element.appendChild(eNoteKeywordsFarsi)


        #<mods:subject><mods:hierarchicalGeographic><mods:country lang="eng">
    if 'Country (English)' in row:
        if row['Country (English)']:
            eCountrySubject = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            eCountryHierarchicalGeographic = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:hierarchicalGeographic')
            ecountry = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:country')
            ecountry.appendChild(newdoc.createTextNode(row['Country (English)'].strip()))
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
            ecountryFarsi.appendChild(newdoc.createTextNode(row['Country (Farsi)'].strip()))
            ecountryFarsi.setAttribute('lang', 'per')
            eCountryHierarchicalGeographicFarsi.appendChild(ecountryFarsi)
            eCountrySubjectFarsi.appendChild(eCountryHierarchicalGeographicFarsi)
            top_element.appendChild(eCountrySubjectFarsi)

        #//<mods:subject><mods:hierarchicalGeographic><mods:city lang="eng">
    if 'City (English-LCSH)' in row:
        if row['City (English-LCSH)']:
            ecitySubject = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            ecityHierarchicalGeographic = newdoc.createElementNS('http://www.loc.gov/mods/v3',
                                                                 'mods:hierarchicalGeographic')
            ecity = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:city')
            ecity.appendChild(newdoc.createTextNode(row['City (English-LCSH)'].strip()))
            ecity.setAttribute('lang', 'eng')
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

        #<mods:subject><mods:hierarchicalGeographic><mods:area lang="eng">
    if 'Place (English)' in row:
        if row['Place (English)']:
            eplaceSubject = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            eplaceHierarchicalGeographic = newdoc.createElementNS('http://www.loc.gov/mods/v3',
                                                                  'mods:hierarchicalGeographic')
            eplace = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:area')
            eplace.appendChild(newdoc.createTextNode(row['Place (English)'].strip()))
            eplace.setAttribute('lang', 'eng')
            eplaceHierarchicalGeographic.appendChild(eplace)
            eplaceSubject.appendChild(eplaceHierarchicalGeographic)
            top_element.appendChild(eplaceSubject)
    if 'Place (Farsi)' in row:
        if row['Place (Farsi)']:
            eplaceSubjectFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
            eplaceHierarchicalGeographicFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3',
                                                                       'mods:hierarchicalGeographic')
            eplaceFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:area')
            eplaceFarsi.appendChild(newdoc.createTextNode(row['Place (Farsi)'].strip()))
            eplaceFarsi.setAttribute('lang', 'per')
            eplaceHierarchicalGeographicFarsi.appendChild(eplaceFarsi)
            eplaceSubjectFarsi.appendChild(eplaceHierarchicalGeographicFarsi)
            top_element.appendChild(eplaceSubjectFarsi)
    if 'Date (Normalized)' in row:
        if row['Date (Normalized)']:
            eOriginInfoDateNormalized = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
            eDateCreatedNormalized = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:dateCreated')
            eDateCreatedNormalized.appendChild(newdoc.createTextNode(row['Date (Normalized)'].strip()))
            eDateCreatedNormalized.setAttribute('encoding','iso8601')
            eOriginInfoDateNormalized.appendChild(eDateCreatedNormalized)
            top_element.appendChild(eOriginInfoDateNormalized)
    if 'Date (Gregorian)' in row:
        if row['Date (Gregorian)']:
            eOriginInfoDateGregorian = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
            eDateCreatedGregorian = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:dateCreated')
            eDateCreatedGregorian.appendChild(newdoc.createTextNode(row['Date (Gregorian)'].strip()))
            eDateCreatedGregorian.setAttribute('lang', 'eng')
            eOriginInfoDateGregorian.appendChild(eDateCreatedGregorian)
            top_element.appendChild(eOriginInfoDateGregorian)
    if 'Date (Farsi)' in row:
        if row['Date (Farsi)']:
            eOriginInfoDateFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
            eDateCreatedFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:dateCreated')
            eDateCreatedFarsi.appendChild(newdoc.createTextNode(row['Date (Farsi)'].strip()))
            eDateCreatedFarsi.setAttribute('lang', 'per')
            eOriginInfoDateFarsi.appendChild(eDateCreatedFarsi)
            top_element.appendChild(eOriginInfoDateFarsi)

        #mods:identifier type=local
    if 'filename' in row:
        if row['filename']:
            eidentifier = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:identifier')
            eidentifier.appendChild(newdoc.createTextNode(row['filename'].strip()))
            eidentifier.setAttribute('type', 'local')
            top_element.appendChild(eidentifier)

    print(newdoc.toprettyxml())

    with open(r'\\svm-netapp-dlib.in.library.ucla.edu\DLIngest\gm_rasatv1\mods\{}.xml'.format(row['filename'].strip()), 'w', encoding='utf-8') as f:
        f.write(newdoc.toprettyxml())



if __name__ == '__main__': main()

