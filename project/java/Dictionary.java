package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  "A dictionary is list of (term/key, value) pairs with each term/key existing no more than once."
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Dictionary extends UcoInherentCharacterizationThing {

  private List<DictionaryEntry> entry;

}