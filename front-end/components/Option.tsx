import * as React from 'react';
import { View } from 'react-native';
import { RadioButton } from 'react-native-paper';

const Option = () => {
  const [checked, setChecked] = React.useState('first');
  
  const test = "Test";

  return (
    <View>
      <RadioButton
        value={test}
        status={ checked === 'first' ? 'checked' : 'unchecked' }
        onPress={() => setChecked('first')}
      />
      <RadioButton
        value="second"
        status={ checked === 'second' ? 'checked' : 'unchecked' }
        onPress={() => setChecked('second')}
      />
    </View>
  );
};

export default Option;
