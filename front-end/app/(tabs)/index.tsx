import { Image, StyleSheet, Text, Pressable, FlatList } from 'react-native';

import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import { Link } from 'expo-router';


const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'Group 1',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Group 2',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Group 3',
  },
];

export default function HomeScreen() {
  return (
    <ParallaxScrollView
      headerBackgroundColor={{ light: '#A1CEDC', dark: '#1D3D47' }}
      headerImage={
        <Image
          //source={require('@/assets/images/Home-Page-Header-Image.jpg')}
        />
      }>
      <ThemedView style={styles.titleContainer}>
        <ThemedText type="title">STUDY APP</ThemedText>
      </ThemedView>
      <FlatList
        data={DATA}

        renderItem={({ item }) =>
          <Link href="/questions" asChild>
            <Pressable>
              <ThemedText>{item.title}</ThemedText>
            </Pressable>
          </Link>
        }


        keyExtractor={item => item.id}
      />
    </ParallaxScrollView>
  );
}

const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
});
