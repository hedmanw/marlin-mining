# Performing tasks

## Manual unstructured merging
I use the Eclipse C IDE to launch inside RCPTT, this will be referred to as the AUT (application under test), since RCPTT is really a testing tool.
The setup instructions are shown [here](https://www.youtube.com/watch?v=prXLW38mk8g) if you prefer a video. Point 6 is not included in the video though.

1. Download Eclipse [RCPTT](http://www.eclipse.org/rcptt/download/).
2. Launch RCPTT
3. Select a workspace for RCPTT
4. Create a new project under File -> New -> RCP Testing Tool Project
5. After the project is created, open the "Project Settings" file. Under "Default Contexts", create a new Workspace which will be used by the AUT.
6. The new Workspace context file will be opened, in this, create a new project and import the directories in `tasks/`. Tick the "Clear workspace" checkbox.
7. In the project, create a new "Test case" by New -> Test case. The new test case definition file will be opened.
8. In the "Applications panel", at the bottom of the screen, right click and select "New...". You will be prompted to point to an Eclipse installation (e.g. Eclipse C IDE).
9. This new application will be added to the same panel. Right click it, and select "Run". Save any changes to files. The AUT will be launched.

Recording actions in the AUT:

1. Ensure that the AUT is running through RCPTT, as above.
2. In the RCPTT instance, open your test case. In the upper left, there is a "Record" button. Press it to start recording.
3. The RCPTT instance will minimize, and action in the AUT is recorded.
4. To stop recording, press the red circle in the RCPTT instance.

Example merging [Taken from here.](http://stackoverflow.com/questions/4623564/how-do-i-compare-two-files-using-eclipse-is-there-any-option-provided-by-eclips):

1. Start recording as above.
2. Select the mainline file and the clone file you want to merge.
3. Right click and select Compare With -> Each other.
4. A two-way diff view is opened. The files can be swapped from left to right if they are on the opposite side.
5. Perform the editing as instructed, and save the result file so we can compare the outcome.
6. Stop recording and save the script so we can analyze the edit operations.

## MPS

1. Import into ppmerge
2. Open in MPS