import { Image, StyleSheet, Platform, Button, FlatList, Pressable } from 'react-native';
import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import Option from '@/components/Option';


const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'Question 1',
    options: ['Answer', 'Answer', 'Answer', 'Answer']
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Question 2',
    options: ['Answer', 'Answer', 'Answer', 'Answer']
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Question 3',
    options: ['Answer', 'Answer', 'Answer', 'Answer']
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

      <FlatList
        data={DATA}

        renderItem={({ item }) =>
          <ThemedView>
            <ThemedText type='subtitle'>{item.title}</ThemedText>
            <form>
              <input type="radio" name={item.id} id="" />
              <ThemedText>{item.options[0]}</ThemedText><br />
              <input type="radio" name={item.id} id="" />
              <ThemedText>{item.options[1]}</ThemedText><br />
              <input type="radio" name={item.id} id="" />
              <ThemedText>{item.options[2]}</ThemedText><br />
              <input type="radio" name={item.id} id="" />
              <ThemedText>{item.options[3]}</ThemedText><br /><br />
              
            </form>
        
          </ThemedView>
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


