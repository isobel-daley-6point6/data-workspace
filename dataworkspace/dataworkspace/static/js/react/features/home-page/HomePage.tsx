import { MEDIA_QUERIES, SPACING_POINTS } from '@govuk-react/constants';
import styled from 'styled-components';

import { FetchDataContainer, InnerContainer, Main } from '../../components';
import { GREY_4 } from '../../constants';
import {
  fetchRecentCollections,
  fetchRecentItems,
  fetchYourBookmarks,
  fetchYourRecentTools
} from '../../services';
import SupportYou from '../support/Support';
import RecentCollections from './components/RecentCollections';
import RecentItems from './components/RecentItems';
import RecentTools from './components/RecentTools';
import YourBookmarks from './components/YourBookmarks';

const StyledMain = styled(Main)`
  background-color: ${GREY_4};
  margin-bottom: ${SPACING_POINTS['6']}px;
  > div {
    display: grid;
    grid-template-columns: 1fr;
    ${MEDIA_QUERIES.TABLET} {
      grid-template-columns: 1fr 1fr;
    }
    grid-gap: ${SPACING_POINTS['6']}px;
  }
`;

const StyledInnerContainer = styled(InnerContainer)`
  margin-bottom: ${SPACING_POINTS['9']}px;
`;

const HomePage = () => {
  return (
    <>
      <StyledMain>
        <FetchDataContainer fetchApi={() => fetchRecentItems()}>
          {(data) => <RecentItems items={data} />}
        </FetchDataContainer>
        <FetchDataContainer fetchApi={() => fetchRecentCollections()}>
          {(data) => <RecentCollections collections={data} />}
        </FetchDataContainer>
        <FetchDataContainer fetchApi={() => fetchYourRecentTools()}>
          {(data) => <RecentTools tools={data} />}
        </FetchDataContainer>
        <FetchDataContainer fetchApi={() => fetchYourBookmarks()}>
          {(data) => <YourBookmarks bookmarks={data} />}
        </FetchDataContainer>
      </StyledMain>
      <StyledInnerContainer>
        <SupportYou />
      </StyledInnerContainer>
    </>
  );
};

export default HomePage;
