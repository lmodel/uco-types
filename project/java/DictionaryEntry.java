package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  "A dictionary entry is a single (term/key, value) pair."
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DictionaryEntry extends UcoInherentCharacterizationThing {

  private String key;
  private String value;

}