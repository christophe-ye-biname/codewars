public class BlueAndRedMarbles {
    public static double guessBlue(int blueStart, int redStart, int bluePulled, int redPulled) {
      // Place your code here
      return (blueStart - bluePulled) / double(redStart - redPulled);
    }
  }