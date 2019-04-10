import xml.etree.ElementTree as ET
from xml.dom.minidom import getDOMImplementation

import csv



# this program can be used for newpapers and posters too.
#csvFile = 'myData.csv'
#csvData = csv.reader(open(csvFile))
def main():
    with open(r'\\svm-netapp-dlib.in.library.ucla.edu\DLIngest\gm_ashraf_photos\gm_ashraf_photos_metadata.csv',
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

    elRelatedItem = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:relatedItem')
    elRelatedItem.setAttribute('type','host')
    eTitleInfoCollectionName = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
    eTitleCollectionName = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
    eTitleCollectionName.appendChild(newdoc.createTextNode('Green Movement (Iran)'))
    eTitleInfoCollectionName.appendChild(eTitleCollectionName)
    elRelatedItem.appendChild(eTitleInfoCollectionName)
    top_element.appendChild(elRelatedItem)

    elProgramRelatedItem = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:relatedItem')
    elProgramRelatedItem.setAttribute('type', 'program')
    eTitleInfoProgramName = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
    eTitleProgramName = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
    eTitleProgramName.appendChild(newdoc.createTextNode('International Digital Ephemera Project'))
    eTitleInfoProgramName.appendChild(eTitleProgramName)
    elProgramRelatedItem.appendChild(eTitleInfoProgramName)
    top_element.appendChild(elProgramRelatedItem)

    eNameRepository = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:relatedItem')
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

    print(row['filename'], row['Genre (English)'])
    if row['Title (English)']:
        elTitleInfo = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
        eTitle = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
        eTitle.appendChild(newdoc.createTextNode(row['Title (English)'].strip()))
        eTitle.setAttribute('lang', 'eng')
        elTitleInfo.appendChild(eTitle)
        top_element.appendChild(elTitleInfo)

    if row['Title (Farsi)']:
        elTitleInfoFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:titleInfo')
        eTitleFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:title')
        eTitleFarsi.appendChild(newdoc.createTextNode(row['Title (Farsi)'].strip()))
        eTitleFarsi.setAttribute('lang', 'per')
        elTitleInfoFarsi.appendChild(eTitleFarsi)
        top_element.appendChild(elTitleInfoFarsi)

    if row['Genre (English)']:
        eGenre = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:genre')
        eGenre.appendChild(newdoc.createTextNode(row['Genre (English)'].strip()))
        eGenre.setAttribute('lang', 'eng')
        top_element.appendChild(eGenre)

    if row['Genre (Farsi)']:
        eGenreFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:genre')
        eGenreFarsi.appendChild(newdoc.createTextNode(row['Genre (Farsi)'].strip()))
        eGenreFarsi.setAttribute('lang', 'per')
        top_element.appendChild(eGenreFarsi)

    if row['Lat, Lon']:
        eLatLonSubject = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
        eLatLonCartographics = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:cartographics')
        eLatLoncoordinates = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:coordinates')
        eLatLoncoordinates.appendChild(newdoc.createTextNode(row['Lat, Lon'].strip()))
        eLatLonCartographics.appendChild(eLatLoncoordinates)
        eLatLonSubject.appendChild(eLatLonCartographics)
        top_element.appendChild(eLatLonSubject)

    if row['Physical Type']:
        eExtent = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:typeOfResource')
        eExtent.appendChild(newdoc.createTextNode(row['Physical Type'].strip()))
        top_element.appendChild(eExtent)


    #<mods:note lang="eng">
    if row['Description (English)']:
        eNoteDescription = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
        eNoteDescription.appendChild(newdoc.createTextNode(row['Description (English)'].strip()))
        eNoteDescription.setAttribute('lang', 'eng')
        top_element.appendChild(eNoteDescription)

    if row['Description (Farsi)']:
        eNoteDescriptionFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
        eNoteDescriptionFarsi.appendChild(newdoc.createTextNode(row['Description (Farsi)'].strip()))
        eNoteDescriptionFarsi.setAttribute('lang', 'per')
        top_element.appendChild(eNoteDescriptionFarsi)

    # //<mods:note lang="eng" displayLabel="Names">
    if row['Names (English)']:
       namesEnglishData = row['Names (English)'].split(' / ')
       for data in namesEnglishData:
           eNoteNames = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
           eNoteNames.appendChild(newdoc.createTextNode(data.strip()))
           eNoteNames.setAttribute('lang', 'eng')
           eNoteNames.setAttribute('displayLabel', 'Names')
           top_element.appendChild(eNoteNames)


    #//<mods:note lang="per" displayLabel="Names">
    if row['Names (Farsi)']:
        namesFarsiData = row['Names (Farsi)'].split(' / ')
        for data in namesFarsiData:
            eNoteNamesFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
            eNoteNamesFarsi.appendChild(newdoc.createTextNode(data.strip()))
            eNoteNamesFarsi.setAttribute('lang','per')
            eNoteNamesFarsi.setAttribute('displayLabel','Names')
            top_element.appendChild(eNoteNamesFarsi)



    #<mods:note lang="eng" displayLabel="Keywords/Chants/Slogans">
    if row['Keywords/Chants/Slogans (English)']:
       keywordsData = row['Keywords/Chants/Slogans (English)'].split(' / ')
       for data in keywordsData:
           eNoteKeywords = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
           eNoteKeywords.appendChild(newdoc.createTextNode(data.strip()))
           eNoteKeywords.setAttribute('lang', 'eng')
           eNoteKeywords.setAttribute('displayLabel', 'Keywords/Chants/Slogans')
           top_element.appendChild(eNoteKeywords)

    if row['Keywords/Chants/Slogans (Farsi)']:
        keywordFarsiData = row['Keywords/Chants/Slogans (Farsi)'].split(' / ')
        for data in keywordFarsiData:
            eNoteKeywordsFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:note')
            eNoteKeywordsFarsi.appendChild(newdoc.createTextNode(data.strip()))
            eNoteKeywordsFarsi.setAttribute('lang', 'per')
            eNoteKeywordsFarsi.setAttribute('displayLabel', 'Keywords/Chants/Slogans')
            top_element.appendChild(eNoteKeywordsFarsi)



    #<mods:subject><mods:hierarchicalGeographic><mods:country lang="eng">
    if row['Country (English)']:
        eCountrySubject = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
        eCountryHierarchicalGeographic = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:hierarchicalGeographic')
        ecountry = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:country')
        ecountry.appendChild(newdoc.createTextNode(row['Country (English)'].strip()))
        ecountry.setAttribute('lang','eng')
        eCountryHierarchicalGeographic.appendChild(ecountry)
        eCountrySubject.appendChild(eCountryHierarchicalGeographic)
        top_element.appendChild(eCountrySubject)

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

    if row['City (Farsi)']:
        ecitySubjectFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:subject')
        ecityHierarchicalGeographicFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3',
                                                                     'mods:hierarchicalGeographic')
        ecityFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:city')
        ecityFarsi.appendChild(newdoc.createTextNode(row['City (Farsi)'].strip()))
        ecityFarsi.setAttribute('lang', 'per')
        ecityHierarchicalGeographicFarsi.appendChild(ecityFarsi)
        ecitySubjectFarsi.appendChild(ecityHierarchicalGeographicFarsi)
        top_element.appendChild(ecitySubjectFarsi)

     #<mods:subject><mods:hierarchicalGeographic><mods:area lang="eng">
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

    if row['Date (Normalized)']:
        eOriginInfoDateNormalized = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
        eDateCreatedNormalized = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:dateCreated')
        eDateCreatedNormalized.appendChild(newdoc.createTextNode(row['Date (Normalized)'].strip()))
        eDateCreatedNormalized.setAttribute('encoding','iso8601')
        eOriginInfoDateNormalized.appendChild(eDateCreatedNormalized)
        top_element.appendChild(eOriginInfoDateNormalized)

    if row['Date (Gregorian)']:
        eOriginInfoDateGregorian = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
        eDateCreatedGregorian = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:dateCreated')
        eDateCreatedGregorian.appendChild(newdoc.createTextNode(row['Date (Gregorian)'].strip()))
        eDateCreatedGregorian.setAttribute('lang', 'eng')
        eOriginInfoDateGregorian.appendChild(eDateCreatedGregorian)
        top_element.appendChild(eOriginInfoDateGregorian)

    if row['Date (Farsi)']:
        eOriginInfoDateFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:originInfo')
        eDateCreatedFarsi = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:dateCreated')
        eDateCreatedFarsi.appendChild(newdoc.createTextNode(row['Date (Farsi)'].strip()))
        eDateCreatedFarsi.setAttribute('lang', 'per')
        eOriginInfoDateFarsi.appendChild(eDateCreatedFarsi)
        top_element.appendChild(eOriginInfoDateFarsi)

    #mods:identifier type=local
    if row['filename']:
        eidentifier = newdoc.createElementNS('http://www.loc.gov/mods/v3', 'mods:identifier')
        eidentifier.appendChild(newdoc.createTextNode(row['filename'].strip()))
        eidentifier.setAttribute('type', 'local')
        top_element.appendChild(eidentifier)

    print(newdoc.toprettyxml())

    with open(r'\\svm-netapp-dlib.in.library.ucla.edu\DLIngest\gm_ashraf_photos\mods\{}.xml'.format(row['filename'].strip()), 'w', encoding='utf-8') as f:
        f.write(newdoc.toprettyxml())



if __name__ == '__main__': main()

