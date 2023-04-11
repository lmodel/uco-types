package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  "A hash is a grouping of characteristics unique to the result of applying a mathematical algorithm that maps data of arbitrary size to a bit string (the 'hash') and is a one-way function, that is, a function which is practically infeasible to invert. This is commonly used for integrity checking of data. [based on https://en.wikipedia.org/wiki/Cryptographic_hash_function]"
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Hash extends UcoInherentCharacterizationThing {

  private String hashValue;
  private String hashMethod;

}