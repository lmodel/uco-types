package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  "A ThreadItem is a member of a thread."
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ThreadItem  {

  private List<CoItem> itemContent;

}