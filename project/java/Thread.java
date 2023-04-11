package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  "A semi-ordered array of items, that can be present in multiple copies.  Implemetation of a UCO Thread is similar to a Collections Ontology List, except a Thread may fork and merge - that is, one of its members may have two or more direct successors, and two or more direct predecessors."
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Thread extends Bag {

  private List<ThreadItem> item;

}