package DAOInterfaces;

import logicClasses.Mark;

import java.util.List;

public interface PhonesReadDAO {
    List<Mark> getALLMarks();
    Mark getPhoneByMark(String phoneMarkName);
    boolean deleteMarkFromData(String PhoneMarkName);
    boolean changeMarkName(String prevName, String nextName);
    boolean addMark(String markName);
}
